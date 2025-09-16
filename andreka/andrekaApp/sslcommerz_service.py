import requests
import json
from django.conf import settings
from .models import Payment, Order, OrderItem

class SSLCOMMERZPaymentService:
    def __init__(self):
        self.sandbox_mode = getattr(settings, 'SSLCOMMERZ_SANDBOX_MODE', True)
        
        if self.sandbox_mode:
            self.store_id = getattr(settings, 'SSLCOMMERZ_SANDBOX_STORE_ID', 'andre68c98db48ae54')
            self.store_password = getattr(settings, 'SSLCOMMERZ_SANDBOX_STORE_PASSWORD', 'andre68c98db48ae54@ssl')
            self.base_url = 'https://sandbox.sslcommerz.com'
        else:
            self.store_id = getattr(settings, 'SSLCOMMERZ_STORE_ID', 'andre68c98db48ae54')
            self.store_password = getattr(settings, 'SSLCOMMERZ_STORE_PASSWORD', 'andre68c98db48ae54@ssl')
            self.base_url = 'https://securepay.sslcommerz.com'
        
        self.init_url = f"{self.base_url}/gwprocess/v4/api.php"
        self.validation_url = f"{self.base_url}/validator/api/validationserverAPI.php"
    
    def create_payment(self, order, amount, customer_info):
        """Create SSLCOMMERZ payment session"""
        try:
            # Generate unique transaction ID
            import uuid
            tran_id = f"ORDER_{order.id}_{uuid.uuid4().hex[:8]}"
            
            # Create payment record
            payment = Payment.objects.create(
                order=order,
                payment_method='sslcommerz',
                amount=amount,
                payment_id=tran_id,
                status='pending'
            )
            
            # Prepare payment data
            payment_data = {
                'store_id': self.store_id,
                'store_passwd': self.store_password,
                'total_amount': str(amount),
                'currency': 'BDT',
                'tran_id': tran_id,
                'success_url': f"{settings.BASE_URL}/payment/sslcommerz/success/",
                'fail_url': f"{settings.BASE_URL}/payment/sslcommerz/fail/",
                'cancel_url': f"{settings.BASE_URL}/payment/sslcommerz/cancel/",
                'ipn_url': f"{settings.BASE_URL}/payment/sslcommerz/ipn/",
                
                # Customer Information
                'cus_name': customer_info.get('name', order.user.get_full_name() or order.user.username),
                'cus_email': customer_info.get('email', order.user.email or 'arifafjr17@gmail.com'),
                'cus_add1': order.shipping_address_line_1,
                'cus_add2': order.shipping_address_line_2 or '',
                'cus_city': order.shipping_city,
                'cus_state': order.shipping_state,
                'cus_postcode': order.shipping_postal_code,
                'cus_country': order.shipping_country,
                'cus_phone': customer_info.get('phone', '+8801878125712'),
                
                # Shipping Information
                'shipping_method': 'YES',  # Required field
                'ship_name': f"{order.shipping_first_name} {order.shipping_last_name}",
                'ship_add1': order.shipping_address_line_1,
                'ship_add2': order.shipping_address_line_2 or '',
                'ship_city': order.shipping_city,
                'ship_state': order.shipping_state,
                'ship_postcode': order.shipping_postal_code,
                'ship_country': order.shipping_country,
                
                # Product Information
                'product_name': ', '.join([item.product_name for item in order.items.all()]),
                'product_category': 'Fashion',
                'product_profile': 'general',
                
                # Additional parameters
                'value_a': f"Order_{order.id}",
                'value_b': f"User_{order.user.id}",
                'value_c': 'SSLCOMMERZ_Payment',
                'value_d': 'Online_Store',
                
                # Required SSLCOMMERZ fields
                'multi_card_name': 'brac_visa,dbbl_visa,ebl_visa,city_visa,standard_visa,hsbc_visa,habib_visa,asia_visa,trust_visa,premier_visa,onecard_visa,ucb_visa,mutual_visa,brtb_visa,credit_visa,ific_visa,agrani_visa,brac_master,dbbl_master,ebl_master,city_master,standard_master,hsbc_master,habib_master,asia_master,trust_master,premier_master,onecard_master,ucb_master,mutual_master,brtb_master,credit_master,ific_master,agrani_master',
                'emi_option': '0',
                'emi_max_inst_option': '9',
                'emi_selected_inst': '0',
                'emi_allow_only': '0',
            }
            
            # Add individual product information (SSLCOMMERZ requires this)
            for i, item in enumerate(order.items.all(), 1):
                payment_data[f'product_name_{i}'] = item.product_name
                payment_data[f'product_category_{i}'] = 'Fashion'
                payment_data[f'product_profile_{i}'] = 'general'
                payment_data[f'amount_{i}'] = str(item.product_price * item.quantity)
                payment_data[f'quantity_{i}'] = str(item.quantity)
            
            # Make API request
            response = requests.post(self.init_url, data=payment_data, timeout=30)
            
            if response.status_code == 200:
                try:
                    result = response.json()
                    
                    if result.get('status') == 'SUCCESS':
                        gateway_url = result.get('GatewayPageURL')
                        session_key = result.get('sessionkey')
                        
                        return {
                            'success': True,
                            'payment': payment,
                            'session_key': session_key,
                            'gateway_url': gateway_url,
                            'tran_id': tran_id
                        }
                    else:
                        error_msg = result.get('failedreason', 'Payment creation failed')
                        return {
                            'success': False,
                            'message': error_msg
                        }
                except Exception as json_error:
                    return {
                        'success': False,
                        'message': f'Invalid JSON response: {response.text}'
                    }
            else:
                return {
                    'success': False,
                    'message': f'HTTP Error: {response.status_code} - {response.text}'
                }
                
        except Exception as e:
            return {
                'success': False,
                'message': str(e)
            }
    
    def validate_payment(self, val_id):
        """Validate payment with SSLCOMMERZ"""
        try:
            validation_data = {
                'val_id': val_id,
                'store_id': self.store_id,
                'store_passwd': self.store_password,
                'format': 'json'
            }
            
            response = requests.post(self.validation_url, data=validation_data, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                return {
                    'success': True,
                    'status': result.get('status'),
                    'data': result
                }
            else:
                return {
                    'success': False,
                    'message': f'HTTP Error: {response.status_code}'
                }
                
        except Exception as e:
            return {
                'success': False,
                'message': str(e)
            }
