# pseudocódigo para MAS-OPL - Módulo Detección Subestimación (D_Subest)

from datetime import datetime, timedelta
import math

class Subestimation_Detection_Module:
    
    def __init__(self, base_canon: float, fatal_deadline_hrs: int = 72):
        self.CANON_BASE = base_canon
        self.FATAL_DEADLINE_HRS = fatal_deadline_hrs
        self.LAMBDA = 0.005 # Factor de crecimiento causal (ajustable si es necesario)
        self.START_TIME = datetime.now() # Momento de envío de la propuesta CSLE
        self.last_alerted_day = 0 # CORRECCIÓN: Inicialización para el anti-spam de alertas

    def get_current_canon(self) -> float:
        """Calcula el Canon de Acceso Causal en el tiempo actual."""
        
        time_elapsed = datetime.now() - self.START_TIME
        time_elapsed_hrs = time_elapsed.total_seconds() / 3600
        
        # El plazo fatal no tiene penalización
        if time_elapsed_hrs <= self.FATAL_DEADLINE_HRS:
            return self.CANON_BASE
        
        # Tiempo de penalización (t - t_Base)
        penalty_time_hrs = time_elapsed_hrs - self.FATAL_DEADLINE_HRS
        
        # Aplicación de la fórmula exponencial
        canon_t = self.CANON_BASE * math.exp(self.LAMBDA * penalty_time_hrs)
        
        if penalty_time_hrs > 0:
            self.trigger_subestimation_alert(penalty_time_hrs)
        return canon_t

    def trigger_subestimation_alert(self, penalty_time_hrs: float):
        """Genera una alerta formal por cada día de retraso en el CSLE."""
        
        days_delayed = math.ceil(penalty_time_hrs / 24)
        current_canon = self.get_current_canon()
        
        # Alerta formal (Ejecutada en el VCU - Vector de Contacto Único)
        if days_delayed > self.last_alerted_day:
            print(f"ALERTA D_SUBEST: Retraso Causal Día {days_delayed}")
            print(f"El Canon de Acceso Causal ha sido re-evaluado y ahora es: {current_canon:.2f}")
            # Actualizar el día para evitar spam
            self.last_alerted_day = days_delayed