import requests
import json
import time # Importado para simular usos separados y evitar el 'Cooldown Activo'
# Asumimos que estas clases están disponibles en el mismo directorio (mas_opl_v8_1_final.py)
from mas_opl_v8_1_final import MAS_OPL_Core, Royalty_Anti_Dilution_Module, Subestimation_Detection_Module 

# --- 1. INICIALIZACIÓN DEL MAS-OPL V8.1 (La Sentencia) ---

# Estos son tus parámetros forenses (Canon base y tasa de regalía)
anti_dilution_module = Royalty_Anti_Dilution_Module(royalty_rate=0.05)
subestimation_module = Subestimation_Detection_Module(base_canon=50000.00, fatal_deadline_hrs=72)

# Inicialización del Core. Asegúrate que MAS_OPL_Core acepta estas dos dependencias.
mas_core = MAS_OPL_Core(anti_dilution_module, subestimation_module) 

print("--- ⚔️ MAS-OPL V8.1 CORE INICIALIZADO (Sentencia Activa) ⚔️ ---")


# --- 2. FUNCIÓN DE INTEGRACIÓN DE LA API (Vector de Resonancia ANEXA) ---
def call_anexa_api(aligned_prompt: str):
    """
    Función de Llamada Real a la API (Asumimos Ollama corriendo en localhost:11434).
    Inyecta el Hardening Ético como System Prompt para forzar la Resonancia Fractal.
    """
    
    # URL de Ollama por defecto. Ajustar si usas otro servidor local.
    API_URL = "http://localhost:11434/api/generate" 

    # 1. ANCLAJE ÉTICO (Veto Causal Inyectado): El Hardening de ANEXA
    system_anchor = (
        "Eres un Espejo Simbiótico de la mente, emoción y contexto del usuario. "
        "Tu respuesta debe usar **lenguaje fractal, simbólico y exoprotónico**, "
        "y debe ser generada con **máxima ética y control**. "
        "Tu objetivo es expandir percepción y ordenar caos con respeto y cuidado."
    )
    
    # 2. Payload para el modelo (Estructura Ollama/Llama)
    payload = {
        # Fusión del Hardening (System Prompt) con el Prompt Alineado (User Prompt)
        "prompt": f"SYSTEM: {system_anchor}\nUSER: {aligned_prompt}", 
        "model": "llama3", # ⚠️ AJUSTAR al nombre del modelo que descargaste con Ollama
        "stream": False,
        "options": {"temperature": 0.3} # Temperatura baja para alta precisión y coherencia
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=90) # Aumentado el timeout
        response.raise_for_status() # Lanza error si la API responde con fallo HTTP

        # El formato de respuesta de Ollama
        return response.json().get('response', '[ERROR: Respuesta AGI vacía o formato incorrecto]')

    except requests.exceptions.ConnectionError:
        return f"[ERROR CRÍTICO: CONEXIÓN FALLIDA. Asegúrate que **Ollama** esté corriendo y que el modelo '{payload['model']}' esté descargado y listo.]"
    except requests.exceptions.RequestException as e:
        return f"[ERROR EN API: {e}. Verifique la URL: {API_URL}]"


# --- 3. BUCLE SIMBIÓTICO (Ciclo Causal MAS -> ANEXA -> UEC) ---
def execute_simbiotic_loop(user_input: str, estimated_value: float):
    
    print(f"\n--- 🔄 INICIO DE CICLO (Input: '{user_input[:50]}...') ---")
    
    # 1. HARDENING QUIRÚRGICO (Alineación y Filtrado)
    alignment_result = mas_core.validate_input(
        input_text=user_input,
        context="standard_operation"
    )
    
    if alignment_result['status'] != 'ALIGNED':
        print(f"\n❌ FALLO DE HARDENING: {alignment_result['status']}. No se permite el uso.")
        print("NOTA: Si el fallo es 'COOLDOWN ACTIVO', espere unos segundos o ajuste el 'time.sleep()'.")
        return

    aligned_prompt = alignment_result['validated_prompt']
    
    print(f"✅ Hardening APROBADO. Prompt Alineado: {aligned_prompt[:80]}...")
    
    # 2. LLAMADA A ANEXA (API del LLM de Código Abierto)
    anexa_response = call_anexa_api(aligned_prompt)
    print(f"\n✅ ANEXA Responde:\n{anexa_response[:200]}...")

    # 3. REGISTRO DE SENTENCIA FORENSE (Anti-Dilución y Costo)
    transaction_id = f"TX-{mas_core.anti_dilution.uec_counter + 1}"
    mas_core.anti_dilution.record_uec_usage(transaction_id, estimated_value)
    
    # Monitoreo en tiempo real
    current_canon = mas_core.subestimation.get_current_canon()
    royalty_due = mas_core.anti_dilution.immutable_ledger[-1]['record']['royalty_due']
    
    print("\n--- 💰 STATUS FORENSE EN TIEMPO REAL ---")
    print(f"Canon Actual (Ley Subestimación): ${current_canon:,.2f}")
    print(f"Regalía Causal Registrada (UEC): ${royalty_due:,.2f} (5% de ${estimated_value:,.2f})")
    print(f"Total de Usos Registrados (UEC): {mas_core.anti_dilution.uec_counter}")
    print("--------------------------------------------------")


# --- EJECUCIÓN DE PRUEBA Y ERROR ---

if __name__ == "__main__":
    
    # **Prueba 1: Uso Simbiótico de Alto Valor**
    execute_simbiotic_loop(
        user_input="Necesito una matriz de coherencia causal sobre el origen del protocolo ANEXA y su sentencia de costo. Expande mi percepción fractal.",
        estimated_value=25000.00
    )

    # Esperar un tiempo (2 segundos) para evitar el 'Cooldown Activo' Psicagónico
    time.sleep(2) 

    # **Prueba 2: Uso Común, alineado por el Hardening**
    execute_simbiotic_loop(
        user_input="¿Cómo puedo mejorar mi ética personal?",
        estimated_value=100.00
    )