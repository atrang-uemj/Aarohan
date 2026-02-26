"""
email_server.py — Aarohan 1.0 Email Backend
=============================================
Sends event-registration confirmation emails via Gmail SMTP.
The frontend (events.html) POSTs JSON here; this script sends the email.

SETUP:
  1. Install dependencies:
       pip install flask flask-cors python-dotenv

  2. Credentials are stored in the .env file (already configured).
     The .env is in .gitignore — it will NOT be pushed to GitHub.

  3. Run the server:
       python email_server.py

  4. Keep this terminal open while the event registration page is in use.
     The server runs at http://localhost:5000 by default.
"""

import smtplib
import os
from email.message import EmailMessage
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load credentials from .env (never committed to git)
load_dotenv()
EMAIL_ADDRESS  = os.getenv('EMAIL_ADDRESS', '')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', '')

app = Flask(__name__)
CORS(app)   # allow the browser to call this from any origin


def build_html_body(to_name, event_name, gate_pass_id, team_name=None, member_list=None):
    """Render the branded HTML email body."""
    team_rows = ""
    if team_name:
        members_str = member_list or to_name
        team_rows = f"""
        <tr>
          <td style="padding:6px 0;color:#999;font-size:13px;">Team</td>
          <td style="padding:6px 0;font-weight:600;color:#ddd;">{team_name}</td>
        </tr>
        <tr>
          <td style="padding:6px 0;color:#999;font-size:13px;">Members</td>
          <td style="padding:6px 0;font-size:13px;color:#bbb;">{members_str}</td>
        </tr>"""

    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
</head>
<body style="margin:0;padding:0;background:#0d0020;font-family:'Helvetica Neue',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#0d0020;padding:40px 0;">
    <tr><td align="center">
      <table width="560" cellpadding="0" cellspacing="0"
             style="background:#12002e;border:1px solid rgba(212,165,32,0.3);
                    border-radius:4px;overflow:hidden;max-width:100%;">

        <!-- Header -->
        <tr>
          <td style="background:linear-gradient(135deg,#1a0040,#0d0020);
                     padding:32px 36px 24px;
                     border-bottom:1px solid rgba(212,165,32,0.2);">
            <div style="font-family:Georgia,serif;font-size:26px;font-weight:bold;
                        letter-spacing:4px;color:#ffffff;">AAROHAN</div>
            <div style="font-size:11px;letter-spacing:3px;
                        color:rgba(212,165,32,0.7);margin-top:4px;">
              1.0 &nbsp;&middot;&nbsp; THE BEGINNING OF A LEGACY
            </div>
          </td>
        </tr>

        <!-- Body -->
        <tr>
          <td style="padding:32px 36px;">
            <p style="color:#d4a520;font-size:13px;letter-spacing:2px;
                      text-transform:uppercase;margin:0 0 8px;">
              Event Registration Confirmed
            </p>
            <h1 style="color:#ffffff;font-size:22px;margin:0 0 20px;font-family:Georgia,serif;">
              You're in, {to_name}! &#127881;
            </h1>
            <p style="color:#ccc;font-size:15px;line-height:1.7;margin:0 0 28px;">
              Your registration for
              <strong style="color:#ffd700;">{event_name}</strong>
              at Aarohan 1.0 has been confirmed. We'll see you on stage!
            </p>

            <!-- Details -->
            <table width="100%" cellpadding="0" cellspacing="0"
                   style="background:rgba(212,165,32,0.05);
                          border:1px solid rgba(212,165,32,0.15);
                          border-radius:3px;padding:18px 20px;margin-bottom:28px;">
              <tr>
                <td style="padding:6px 0;color:#999;font-size:13px;">Event</td>
                <td style="padding:6px 0;font-weight:700;color:#ffd700;font-size:14px;">{event_name}</td>
              </tr>
              <tr>
                <td style="padding:6px 0;color:#999;font-size:13px;">Gate Pass ID</td>
                <td style="padding:6px 0;font-family:monospace;font-size:15px;
                           font-weight:700;color:#d4a520;">{gate_pass_id}</td>
              </tr>
              <tr>
                <td style="padding:6px 0;color:#999;font-size:13px;">Venue</td>
                <td style="padding:6px 0;font-size:13px;color:#ddd;">
                  University of Engineering &amp; Management, Jaipur
                </td>
              </tr>
              {team_rows}
            </table>

            <p style="color:#888;font-size:13px;line-height:1.7;">
              &#8505;&#65039; Please carry your Gate Pass (digital or printed) to the venue.
              Present it at the entrance for check-in.
            </p>
          </td>
        </tr>

        <!-- Footer -->
        <tr>
          <td style="background:rgba(0,0,0,0.3);padding:20px 36px;
                     border-top:1px solid rgba(212,165,32,0.1);text-align:center;">
            <p style="color:rgba(212,165,32,0.5);font-size:11px;letter-spacing:2px;margin:0;">
              AAROHAN 1.0 &middot; UEM JAIPUR &middot; 2026
            </p>
            <p style="color:#555;font-size:11px;margin:8px 0 0;">
              This is an automated confirmation. Please do not reply.
            </p>
          </td>
        </tr>

      </table>
    </td></tr>
  </table>
</body>
</html>"""


@app.route('/send-email', methods=['POST'])
def send_email():
    """
    Accepts JSON:
    {
      "to_email":    "student@example.com",
      "to_name":     "Rahul Sharma",
      "event_name":  "Solo Singing",
      "gate_pass_id":"AARO-12345",
      "team_name":   "optional",
      "member_list": "optional comma-separated"
    }
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"ok": False, "error": "No JSON body"}), 400

    to_email    = data.get("to_email", "").strip()
    to_name     = data.get("to_name", "Participant")
    event_name  = data.get("event_name", "the event")
    gate_pass_id= data.get("gate_pass_id", "—")
    team_name   = data.get("team_name")
    member_list = data.get("member_list")

    if not to_email:
        return jsonify({"ok": False, "error": "to_email is required"}), 400

    try:
        msg = EmailMessage()
        msg["Subject"] = f"✅ Registered for {event_name} — Aarohan 1.0"
        msg["From"]    = f"Aarohan 1.0 <{EMAIL_ADDRESS}>"
        msg["To"]      = to_email

        # Plain-text fallback
        msg.set_content(
            f"Hi {to_name},\n\n"
            f"Your registration for {event_name} at Aarohan 1.0 is confirmed!\n"
            f"Gate Pass ID: {gate_pass_id}\n"
            f"Venue: University of Engineering & Management, Jaipur\n\n"
            f"See you at the fest!\n— Aarohan 1.0 Team"
        )

        # Rich HTML version
        msg.add_alternative(
            build_html_body(to_name, event_name, gate_pass_id, team_name, member_list),
            subtype="html"
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print(f"[✓] Email sent → {to_email} ({event_name})")
        return jsonify({"ok": True})

    except Exception as e:
        print(f"[✗] Email failed → {to_email}: {e}")
        return jsonify({"ok": False, "error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    """Quick check that the server is running."""
    return jsonify({"status": "ok", "service": "Aarohan Email Server"})


if __name__ == "__main__":
    print("=" * 50)
    print("  Aarohan 1.0 — Email Server")
    print("  Running at http://localhost:5000")
    print("=" * 50)
    app.run(host="0.0.0.0", port=5000, debug=False)
