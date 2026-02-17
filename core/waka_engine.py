"""
MAWS Core Engine - Waka v1.1
Orchestrateur central avec sécurité Nanashi native.
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from config.settings import settings
    from utils.linkpro import link_pro
    # On importe maintenant l'agent Blinky
    from core.ghosts import blinky
except ImportError as e:
    print(f"Erreur critique d'importation : {e}")
    sys.exit(1)

class WakaEngine:
    def __init__(self):
        self.name = "Waka-Engine"
        self.version = "1.1.0"
        print(f"[{self.name}] Initialisation du système...")
        
        if not link_pro.is_active:
            raise PermissionError("ALERTE: Tunnel LinkPro inactif. Arrêt immédiat.")
        
        print(f"[{self.name}] Tunnel USL-EDL : CONNECTÉ")
        print(f"[{self.name}] Agent Orchestrateur ({blinky.name}) : EN LIGNE")

    def process_query(self, user_input: str):
        """
        Traite une requête en passant par le sas de sécurité puis les agents.
        """
        # 1. USL (Entrée)
        try:
            secure_input = link_pro.usl_ingress(user_input)
        except Exception as e:
            return {"status": "error", "message": str(e)}
        
        # 2. GHOST PROTOCOL (Agents)
        # On demande à Blinky d'analyser la tâche
        print(f"[{self.name}] Transmission à l'orchestrateur...")
        agent_decision = blinky.analyze_task(secure_input)
        
        # On formule la réponse
        raw_response = f"Mission reçue. {agent_decision}"
        
        # 3. EDL (Sortie)
        safe_response = link_pro.edl_egress(raw_response)
        
        return {
            "status": "success",
            "audit_proof": True,
            "response": safe_response
        }

# Instance prête
waka = WakaEngine()
