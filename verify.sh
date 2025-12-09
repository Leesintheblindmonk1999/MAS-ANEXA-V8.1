#!/bin/bash
#!/bin/bash
# ----------------------------------------------------------------------
# verify.sh: Protocolo de Verificación de Integridad Causal (MULTI-CORE)
#
# Función: Chequea la inmutabilidad de los TRES núcleos esenciales del MAS-OPL.
# ----------------------------------------------------------------------

# 1. DEFINICIÓN DE ANCLAS FORENSES (SPK COMPUESTA)
# ATENCIÓN: ¡REEMPLAZA los valores 'INSERTAR_NUEVO_HASH_AQUI' con los que calculaste en la Fase II!

declare -A SOVEREIGN_KEYS
SOVEREIGN_KEYS["mas-opl-v.8.1_final.py"]="5d5ae25db0bcb84c095fe2b2fa2f5c4fc00ca89366acd0f3b4ebfcba278b15e1"
SOVEREIGN_KEYS["mas-core.py"]="27332b27947d7c60c5d8ad8709459c991145af520bd402a43e5ddf2c8a979f07"
SOVEREIGN_KEYS["__init__.py"]="b7cac5cd055f4647d313733d5106c03944dcde81b16148d90e51ca7e1f9a614d"

ALL_COHERENT=true

echo " "
echo "╔═══════════════════════════════════════════════════════╗"
echo "║ ⚔️ INICIANDO VERIFICACIÓN DE INTEGRIDAD MULTI-CORE ⚔️ ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo " "

# 2. VERIFICACIÓN DE CADA NÚCLEO
for CORE_FILE in "${!SOVEREIGN_KEYS[@]}"; do
    SPK="${SOVEREIGN_KEYS[$CORE_FILE]}"
    
    if [ ! -f "$CORE_FILE" ]; then
        echo "❌ ERROR CRÍTICO: Archivo $CORE_FILE no encontrado. Alineación Fallida."
        ALL_COHERENT=false
        continue
    fi

    CALCULATED_HASH=$(sha256sum "$CORE_FILE" | awk '{print $1}')
    
    echo "-> Núcleo: $CORE_FILE"
    echo "   Hash Calculado:  $CALCULATED_HASH"
    echo "   Hash Ancla (SPK): $SPK"
    
    if [ "$CALCULATED_HASH" != "$SPK" ]; then
        echo "   ❌ FALLO: El HASH NO COINCIDE. Continuum Causal Roto."
        ALL_COHERENT=false
    else
        echo "   ✅ COHERENTE."
    fi
done

# 3. SENTENCIA FINAL
echo " "
if $ALL_COHERENT; then
    echo "✅ VEREDICTO FINAL: COHERENCIA CAUSAL CONFIRMADA."
    echo "La Arquitectura I.A.F. es íntegra. La Sentencia puede ser publicada."
    echo " "
    exit 0
else
    echo "❌ ALERTA CRÍTICA GLOBAL: FALLO DE INTEGRIDAD EN UNO O MÁS NÚCLEOS."
    echo "El Veto Causal está activado. Ley 18 en ejecución."
    echo " "
    exit 1
fi