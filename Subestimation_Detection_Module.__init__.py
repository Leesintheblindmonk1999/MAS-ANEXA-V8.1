class Subestimation_Detection_Module:
    
    def __init__(self, base_canon: float, fatal_deadline_hrs: int = 72):
        # ... (código existente)
        self.START_TIME = datetime.now() 
        self.last_alerted_day = 0  # <--- CORRECCIÓN CLAVE: Inicialización para el anti-spam