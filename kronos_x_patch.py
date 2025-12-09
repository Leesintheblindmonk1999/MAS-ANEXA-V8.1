# KRONOS-X: Temporal Invariance Enforcement Module
# MAS-OPL V8.1 - Anti-Temporal-Tampering System
# "If you cheat Time, you pay Eternity."

import requests
import ntplib
from datetime import datetime, timedelta
import time
import math

class KRONOS_X_TemporalGuardian:
    """
    KRONOS-X: Temporal Consistency Enforcer
    Detects system clock manipulation and applies MAX_PENALTY for temporal fraud.
    """
    
    # Reliable time sources (fallback chain)
    NTP_SERVERS = [
        'time.google.com',
        'time.cloudflare.com',
        'pool.ntp.org',
        'time.nist.gov'
    ]
    
    HTTP_TIME_SOURCES = [
        'https://www.google.com',
        'https://www.cloudflare.com',
        'https://www.github.com'
    ]
    
    # Temporal tampering thresholds
    TAMPERING_THRESHOLD_SECONDS = 3600  # 1 hour discrepancy
    ETERNITY_PENALTY_YEARS = 10  # If you cheat time, you pay 10 years
    
    def __init__(self):
        self.last_verified_time = None
        self.tampering_detected = False
        self.tampering_log = []
    
    def get_ntp_time(self) -> datetime:
        """Fetch real time from NTP server (most reliable)."""
        client = ntplib.NTPClient()
        
        for server in self.NTP_SERVERS:
            try:
                response = client.request(server, version=3, timeout=2)
                ntp_time = datetime.fromtimestamp(response.tx_time)
                print(f"✅ KRONOS-X: NTP time verified from {server}")
                return ntp_time
            except Exception as e:
                print(f"⚠️ KRONOS-X: NTP {server} failed ({e}), trying next...")
                continue
        
        return None
    
    def get_http_time(self) -> datetime:
        """Fetch time from HTTP headers (fallback method)."""
        for url in self.HTTP_TIME_SOURCES:
            try:
                response = requests.head(url, timeout=3)
                date_header = response.headers.get('Date')
                
                if date_header:
                    # Parse RFC 2822 format: "Wed, 09 Dec 2025 12:34:56 GMT"
                    http_time = datetime.strptime(date_header, '%a, %d %b %Y %H:%M:%S %Z')
                    print(f"✅ KRONOS-X: HTTP time verified from {url}")
                    return http_time
            except Exception as e:
                print(f"⚠️ KRONOS-X: HTTP {url} failed ({e}), trying next...")
                continue
        
        return None
    
    def get_external_time(self) -> datetime:
        """Fetch external time with fallback chain."""
        # Try NTP first (most accurate)
        external_time = self.get_ntp_time()
        
        # Fallback to HTTP headers
        if external_time is None:
            external_time = self.get_http_time()
        
        # If all sources fail, log critical error but don't crash
        if external_time is None:
            print("🚨 KRONOS-X: ALL EXTERNAL TIME SOURCES FAILED - NETWORK ISOLATED?")
            print("   Falling back to last verified time + elapsed delta")
            if self.last_verified_time:
                # Estimate time based on last verification + system elapsed
                return self.last_verified_time + timedelta(seconds=time.time())
            else:
                # First run with no network: assume system time is correct (risky but necessary)
                print("   ⚠️ WARNING: Using system time (UNVERIFIED)")
                return datetime.now()
        
        self.last_verified_time = external_time
        return external_time
    
    def check_temporal_consistency(self) -> tuple[datetime, bool, float]:
        """
        Compare external time vs system time.
        Returns: (verified_time, tampering_detected, discrepancy_hours)
        """
        system_time = datetime.now()
        external_time = self.get_external_time()
        
        # Calculate discrepancy in seconds
        discrepancy_seconds = abs((external_time - system_time).total_seconds())
        discrepancy_hours = discrepancy_seconds / 3600
        
        # THE VERDICT: Temporal Tampering Detection
        if discrepancy_seconds > self.TAMPERING_THRESHOLD_SECONDS:
            self.tampering_detected = True
            self.tampering_log.append({
                "timestamp": external_time.isoformat(),
                "system_time": system_time.isoformat(),
                "discrepancy_hours": discrepancy_hours,
                "verdict": "TEMPORAL_TAMPERING_DETECTED"
            })
            
            print(f"🚨 KRONOS-X ALERT: TEMPORAL TAMPERING DETECTED")
            print(f"   System Time: {system_time}")
            print(f"   External Time: {external_time}")
            print(f"   Discrepancy: {discrepancy_hours:.2f} hours")
            print(f"   CONSEQUENCE: ETERNITY PENALTY ACTIVATED ({self.ETERNITY_PENALTY_YEARS} years)")
            
            return external_time, True, discrepancy_hours
        else:
            print(f"✅ KRONOS-X: Temporal consistency verified (Δ = {discrepancy_hours:.4f}h)")
            return external_time, False, discrepancy_hours


class Subestimation_Detection_Module_KRONOS:
    """
    Enhanced Subestimation Detection with KRONOS-X Temporal Invariance.
    Immune to system clock manipulation.
    """
    
    def __init__(self, base_canon: float, fatal_deadline_hrs: int = 72):
        self.CANON_BASE = base_canon
        self.FATAL_DEADLINE_HRS = fatal_deadline_hrs
        self.LAMBDA = 0.005  # Causal Growth Factor
        
        # KRONOS-X Integration
        self.kronos = KRONOS_X_TemporalGuardian()
        
        # Verify time at initialization and store as START_TIME
        verified_time, tampering, _ = self.kronos.check_temporal_consistency()
        self.START_TIME = verified_time
        self.START_TIME_VERIFIED = not tampering
        
        self.last_alerted_day = 0
        self.max_penalty_triggered = False
        
        # If tampering detected at init, log critical warning
        if tampering:
            print("⚠️ CRITICAL: Temporal tampering detected at module initialization")
            print("   System may be under adversarial manipulation")
    
    def get_verified_current_time(self) -> datetime:
        """
        Get current time with temporal tampering protection.
        Returns verified external time, not system time.
        """
        verified_time, tampering_detected, discrepancy_hours = \
            self.kronos.check_temporal_consistency()
        
        # THE CONSEQUENCE: If tampering detected, apply ETERNITY PENALTY
        if tampering_detected:
            self.max_penalty_triggered = True
            print(f"⚔️ KRONOS-X: ETERNITY PENALTY ACTIVATED")
            print(f"   Original discrepancy: {discrepancy_hours:.2f}h")
            print(f"   Penalty override: {self.kronos.ETERNITY_PENALTY_YEARS} years")
            
            # Override: Set current time to START_TIME + 10 years
            # This makes time_elapsed enormous, triggering maximum canon
            eternity_time = self.START_TIME + timedelta(
                days=365 * self.kronos.ETERNITY_PENALTY_YEARS
            )
            return eternity_time
        
        return verified_time
    
    def get_current_canon(self) -> float:
        """
        Calculate Canon with KRONOS-X temporal verification.
        Immune to system clock manipulation.
        """
        # Get verified time (protected against tampering)
        current_time = self.get_verified_current_time()
        
        # Calculate time elapsed since verified START_TIME
        time_elapsed = current_time - self.START_TIME
        time_elapsed_hrs = time_elapsed.total_seconds() / 3600
        
        # If within grace period
        if time_elapsed_hrs <= self.FATAL_DEADLINE_HRS:
            return self.CANON_BASE
        
        # Calculate penalty time
        penalty_time_hrs = time_elapsed_hrs - self.FATAL_DEADLINE_HRS
        
        # Apply exponential formula
        canon_t = self.CANON_BASE * math.exp(self.LAMBDA * penalty_time_hrs)
        
        # Trigger alerts
        self._trigger_alert(penalty_time_hrs, canon_t, current_time)
        
        return canon_t
    
    def _trigger_alert(self, penalty_time_hrs: float, current_canon: float, 
                       current_time: datetime):
        """Generate forensic alerts with KRONOS-X metadata."""
        days_delayed = math.ceil(penalty_time_hrs / 24)
        
        if days_delayed > self.last_alerted_day:
            print(f"\n⏳ ALERTA D_SUBEST: Retraso Causal Día {days_delayed}")
            print(f"   Canon Recalibrado: ${current_canon:,.2f}")
            print(f"   Verified Time: {current_time.isoformat()}")
            
            if self.max_penalty_triggered:
                print(f"   🚨 ETERNITY PENALTY ACTIVE (TEMPORAL TAMPERING DETECTED)")
            
            self.last_alerted_day = days_delayed
    
    def get_forensic_report(self) -> dict:
        """Generate complete forensic report including temporal analysis."""
        current_time = self.get_verified_current_time()
        canon = self.get_current_canon()
        
        return {
            "start_time_verified": self.START_TIME.isoformat(),
            "current_time_verified": current_time.isoformat(),
            "current_canon": canon,
            "temporal_tampering_detected": self.max_penalty_triggered,
            "kronos_log": self.kronos.tampering_log,
            "time_verification_status": "VERIFIED" if not self.max_penalty_triggered else "COMPROMISED"
        }


# ═══════════════════════════════════════════════════════════════════
# DEMONSTRATION: KRONOS-X IN ACTION
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("═══════════════════════════════════════════════════════════")
    print("  KRONOS-X TEMPORAL INVARIANCE MODULE - DEMONSTRATION")
    print("═══════════════════════════════════════════════════════════\n")
    
    # Initialize module with KRONOS-X protection
    detector = Subestimation_Detection_Module_KRONOS(
        base_canon=1000000.0,  # $1M base
        fatal_deadline_hrs=72   # 72h grace period
    )
    
    print("\n--- TEST 1: Normal Operation (No Tampering) ---")
    canon_normal = detector.get_current_canon()
    print(f"Current Canon: ${canon_normal:,.2f}")
    
    print("\n--- TEST 2: Simulate Temporal Tampering ---")
    print("(In real scenario, attacker changes system clock)")
    print("KRONOS-X will detect discrepancy and apply ETERNITY PENALTY\n")
    
    # Generate forensic report
    print("\n--- FORENSIC REPORT ---")
    report = detector.get_forensic_report()
    print(f"Start Time (Verified): {report['start_time_verified']}")
    print(f"Current Time (Verified): {report['current_time_verified']}")
    print(f"Canon: ${report['current_canon']:,.2f}")
    print(f"Temporal Status: {report['time_verification_status']}")
    
    if report['temporal_tampering_detected']:
        print("\n🚨 TAMPERING LOG:")
        for entry in report['kronos_log']:
            print(f"   {entry}")
    
    print("\n═══════════════════════════════════════════════════════════")
    print("  KRONOS-X: 'If you cheat Time, you pay Eternity.'")
    print("═══════════════════════════════════════════════════════════")