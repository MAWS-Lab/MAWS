"""
MAWS Core Engine - Waka v1.1
Orchestrateur central avec sécurité Nanashi native.
"""
import sys
import os

# Permet au moteur de trouver les modules dans les dossiers voisins
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from config.settings import settings
    from utils.linkpro import link_pro
except ImportError as e:
    print(f"Erreur critique d'importation : {e}")
    sys.exit(1)

class WakaEngine:
    def __init__(self):
        self.name = "Waka-Engine"
        self.version = "1.1.0"
        print(f"[{self.name}] Initialisation du système...")
        
        # Vérification du tunnel de sécurité (USL-EDL)
        if not link_pro.is_active:
            raise PermissionError("ALERTE: Tunnel LinkPro inactif. Arrêt immédiat.")
        
        print(f"[{self.name}] Tunnel USL-EDL : CONNECTÉ & SÉCURISÉ")

    def process_query(self, user_input: str):
        """
        Traite une requête en passant par le sas de sécurité.
        """
        # 1. USL (Entrée) : On vérifie qui parle
        try:
            secure_input = link_pro.usl_ingress(user_input)
        except Exception as e:
            return {"status": "error", "message": str(e)}
        
        # 2. Logique (Ici, les agents travailleront plus tard)
        print(f"[{self.name}] Traitement de : {secure_input[:20]}...")
        raw_response = f"Traitement confirmé pour : {secure_input}"
        
        # 3. EDL (Sortie) : On nettoie avant de répondre
        safe_response = link_pro.edl_egress(raw_response)
        
        return {
            "status": "success",
            "audit_proof": True, # Prouve que c'est passé par le Bloc 0 (simulé)
            "response": safe_response
        }

# Instance prête
waka = WakaEngine()
