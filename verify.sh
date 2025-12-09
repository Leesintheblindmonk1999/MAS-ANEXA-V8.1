#!/bin/bash
# ----------------------------------------------------------------------
# verify.sh: Protocolo de Verificación de Integridad Causal (MULTI-CORE)
#
# Función: Chequea la inmutabilidad de los 6 núcleos esenciales del MAS-OPL V8.1.
# ----------------------------------------------------------------------

# 1. DEFINICIÓN DE ANCLAS FORENSES (SPK COMPUESTA FINAL)
# HASHES GRABADOS (Alineación Causal Completa)

declare -A SOVEREIGN_KEYS

SOVEREIGN_KEYS["mas-opl-v.8.1_final.py"]="5d5ae25db0bcb84c095fe2b2fa2f5c4fc00ca89366acd0f3b4ebfcba278b15e1"
SOVEREIGN_KEYS["mas-core.py"]="27332b27947d7c60c5d8ad8709459c991145af520bd402a43e5ddf2c8a979f07"
SOVEREIGN_KEYS["__init__.py"]="e93361ab48e9942e6a5875675bdb3975712ed77c74f2d578d0dd70cd5b781c37"
SOVEREIGN_KEYS["Módulo-Anti-Dilución.py"]="c5f5e4acb4a358842b951e9ba459b4447260c0338ed6a17aee9179aa4b65d00a"
SOVEREIGN_KEYS["Módulo Detección-Subestimación.py"]="45a78105633e1687cd6c49045600f1c082099075a8ea72cd4e91959722ca87b4"
SOVEREIGN_KEYS["kronos_x_patch.py"]="b65d3af04b04cd529b5650b6e38c8f8a1783a515d02ae0369b6495c410bca67a"

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

    # Nota: sha256sum en Git Bash puede generar un espacio adicional, se usa awk para limpiar
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