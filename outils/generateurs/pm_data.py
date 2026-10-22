# Les 12 moyens de paiement acceptés : (clé, fichier, nom complet, nom court, type)
PM = [
    ('wave', 'wave', 'Wave', 'Wave', 'mm'),
    ('om', 'orange-money', 'Orange Money', 'Orange Money', 'mm'),
    ('mtn', 'mtn-momo', 'MTN Mobile Money', 'MTN MoMo', 'mm'),
    ('moov', 'moov-money', 'Moov Money', 'Moov Money', 'mm'),
    ('airtel', 'airtel-money', 'Airtel Money', 'Airtel Money', 'mm'),
    ('mixx-tg', 'mixx-tg', 'Mixx by Yas Togo', 'Mixx Togo', 'mm'),
    ('flooz', 'flooz', 'Flooz', 'Flooz', 'mm'),
    ('mixx-sn', 'mixx-sn', 'Mixx by Yas Sénégal', 'Mixx Sénégal', 'mm'),
    ('mpesa', 'm-pesa', 'M-Pesa', 'M-Pesa', 'mm'),
    ('celtiis', 'celtiis', 'Celtiis Cash', 'Celtiis Cash', 'mm'),
    ('visa', 'visa', 'Visa', 'Visa', 'card'),
    ('mastercard', 'mastercard', 'Mastercard', 'Mastercard', 'card'),
]
src = lambda f: f'assets/logos/pm/{f}.webp'
