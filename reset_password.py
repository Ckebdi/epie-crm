"""
Script de secours — réinitialisation d'un mot de passe SANS passer par l'interface.

À utiliser uniquement si l'accès à l'interface est perdu (ex. : mot de passe
directeur oublié). À lancer depuis le dossier de l'application, sur le serveur :

    python reset_password.py <login> <nouveau_mot_de_passe>

Exemple :
    python reset_password.py directeur NouveauMdp2026!

Le compte devra re-changer son mot de passe à la prochaine connexion.
"""
import os
import sys
import sqlite3

from werkzeug.security import generate_password_hash

DB = os.path.join(os.path.dirname(__file__), "epie_crm.db")


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    login, pw = sys.argv[1], sys.argv[2]

    if len(pw) < 8:
        print("Erreur : le mot de passe doit contenir au moins 8 caractères.")
        sys.exit(1)

    if not os.path.exists(DB):
        print(f"Erreur : base introuvable ({DB}). Lancer ce script depuis le dossier de l'application.")
        sys.exit(1)

    conn = sqlite3.connect(DB)
    cur = conn.execute(
        "UPDATE users SET password=?, must_change_pw=1 WHERE login=?",
        (generate_password_hash(pw), login)
    )
    conn.commit()

    if cur.rowcount == 0:
        logins = [r[0] for r in conn.execute("SELECT login FROM users ORDER BY login")]
        print(f"Erreur : aucun compte « {login} ». Comptes existants : {', '.join(logins)}")
        conn.close()
        sys.exit(1)

    # Trace dans le journal d'audit
    try:
        conn.execute(
            "INSERT INTO audit_log (user_login, role, action, details) VALUES (?,?,?,?)",
            ("script", "admin", "Mot de passe réinitialisé (script de secours)", f"login « {login} »")
        )
        conn.commit()
    except Exception:
        pass
    conn.close()

    print(f"OK — mot de passe de « {login} » réinitialisé.")
    print("Le compte devra choisir un nouveau mot de passe à sa prochaine connexion.")


if __name__ == "__main__":
    main()
