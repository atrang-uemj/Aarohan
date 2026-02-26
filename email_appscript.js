/**
 * Aarohan 1.0 — Email Web App (Google Apps Script)
 * =================================================
 * Deploy this as a Web App on script.google.com
 * It receives POST requests from the website and sends
 * confirmation emails using your Google/Gmail account.
 *
 * DEPLOY STEPS (one-time, ~3 minutes):
 *  1. Go to https://script.google.com  → New Project
 *  2. Delete any existing code, paste this entire file
 *  3. Click "Deploy" → "New Deployment"
 *  4. Type: Web App
 *     Execute as: Me
 *     Who has access: Anyone
 *  5. Click Deploy → Authorise (allow Gmail access)
 *  6. Copy the Web App URL — looks like:
 *     https://script.google.com/macros/s/XXXXXXX/exec
 *  7. Paste that URL into events.html as APPS_SCRIPT_URL
 */

// ─── Handle POST ───────────────────────────────────────────
function doPost(e) {
    try {
        var data = JSON.parse(e.postData.contents);
        var toEmail = data.to_email || '';
        var toName = data.to_name || 'Participant';
        var emailType = data.email_type || 'registration';

        if (!toEmail) throw new Error('to_email is required');

        var subject, html, plain;

        if (emailType === 'welcome') {
            subject = 'Welcome to Aarohan 1.0!';
            html = buildWelcomeHtml(toName);
            plain = 'Hi ' + toName + ',\n\nYou have successfully signed in to the Aarohan 1.0 portal.\n' +
                'You can now register for events and view your Gate Passes from the dashboard.\n\n— Aarohan 1.0 Team';
        } else {
            var eventName = data.event_name || 'the event';
            var gatePassID = data.gate_pass_id || '—';
            var teamName = data.team_name || null;
            var memberList = data.member_list || null;

            subject = '✅ Registered for ' + eventName + ' — Aarohan 1.0';
            html = buildHtml(toName, eventName, gatePassID, teamName, memberList);
            plain = 'Hi ' + toName + ',\n\nYou are registered for ' + eventName +
                ' at Aarohan 1.0!\nGate Pass ID: ' + gatePassID +
                '\nVenue: University of Engineering & Management, Jaipur\n\nSee you at the fest!\n— Aarohan 1.0 Team';
        }

        GmailApp.sendEmail(toEmail, subject, plain, { htmlBody: html, name: 'Aarohan 1.0 — UEM Jaipur' });

        return ContentService
            .createTextOutput(JSON.stringify({ ok: true }))
            .setMimeType(ContentService.MimeType.JSON);

    } catch (err) {
        return ContentService
            .createTextOutput(JSON.stringify({ ok: false, error: err.message }))
            .setMimeType(ContentService.MimeType.JSON);
    }
}

// ─── Handle GET (health check) ─────────────────────────────
function doGet() {
    return ContentService
        .createTextOutput(JSON.stringify({ status: 'ok', service: 'Aarohan Email Web App' }))
        .setMimeType(ContentService.MimeType.JSON);
}

// ─── Build HTML email ──────────────────────────────────────
function buildHtml(toName, eventName, gatePassID, teamName, memberList) {
    var teamRows = '';
    if (teamName) {
        teamRows =
            '<tr><td style="padding:6px 0;color:#999;font-size:13px;">Team</td>' +
            '<td style="padding:6px 0;font-weight:600;color:#ddd;">' + teamName + '</td></tr>' +
            '<tr><td style="padding:6px 0;color:#999;font-size:13px;">Members</td>' +
            '<td style="padding:6px 0;font-size:13px;color:#bbb;">' + (memberList || toName) + '</td></tr>';
    }

    return '<!DOCTYPE html><html><head><meta charset="UTF-8"></head>' +
        '<body style="margin:0;padding:0;background:#0d0020;font-family:Arial,sans-serif;">' +
        '<table width="100%" cellpadding="0" cellspacing="0" style="background:#0d0020;padding:40px 0;">' +
        '<tr><td align="center">' +
        '<table width="560" cellpadding="0" cellspacing="0" style="background:#12002e;border:1px solid rgba(212,165,32,0.3);border-radius:4px;overflow:hidden;max-width:100%;">' +

        // Header
        '<tr><td style="background:linear-gradient(135deg,#1a0040,#0d0020);padding:32px 36px 24px;border-bottom:1px solid rgba(212,165,32,0.2);">' +
        '<div style="font-family:Georgia,serif;font-size:26px;font-weight:bold;letter-spacing:4px;color:#fff;">AAROHAN</div>' +
        '<div style="font-size:11px;letter-spacing:3px;color:rgba(212,165,32,0.7);margin-top:4px;">1.0 &nbsp;&middot;&nbsp; THE BEGINNING OF A LEGACY</div>' +
        '</td></tr>' +

        // Body
        '<tr><td style="padding:32px 36px;">' +
        '<p style="color:#d4a520;font-size:13px;letter-spacing:2px;text-transform:uppercase;margin:0 0 8px;">Event Registration Confirmed</p>' +
        '<h1 style="color:#fff;font-size:22px;margin:0 0 20px;font-family:Georgia,serif;">You\'re in, ' + toName + '! &#127881;</h1>' +
        '<p style="color:#ccc;font-size:15px;line-height:1.7;margin:0 0 28px;">Your registration for <strong style="color:#ffd700;">' + eventName + '</strong> at Aarohan 1.0 has been confirmed. We\'ll see you on stage!</p>' +

        // Details table
        '<table width="100%" cellpadding="0" cellspacing="0" style="background:rgba(212,165,32,0.05);border:1px solid rgba(212,165,32,0.15);border-radius:3px;padding:18px 20px;margin-bottom:28px;">' +
        '<tr><td style="padding:6px 0;color:#999;font-size:13px;">Event</td><td style="padding:6px 0;font-weight:700;color:#ffd700;font-size:14px;">' + eventName + '</td></tr>' +
        '<tr><td style="padding:6px 0;color:#999;font-size:13px;">Gate Pass ID</td><td style="padding:6px 0;font-family:monospace;font-size:15px;font-weight:700;color:#d4a520;">' + gatePassID + '</td></tr>' +
        '<tr><td style="padding:6px 0;color:#999;font-size:13px;">Venue</td><td style="padding:6px 0;font-size:13px;color:#ddd;">University of Engineering &amp; Management, Jaipur</td></tr>' +
        teamRows +
        '</table>' +

        '<p style="color:#888;font-size:13px;line-height:1.7;">&#8505;&#65039; Please carry your Gate Pass to the venue. Present it at the entrance for check-in.</p>' +
        '</td></tr>' +

        // Footer
        '<tr><td style="background:rgba(0,0,0,0.3);padding:20px 36px;border-top:1px solid rgba(212,165,32,0.1);text-align:center;">' +
        '<p style="color:rgba(212,165,32,0.5);font-size:11px;letter-spacing:2px;margin:0;">AAROHAN 1.0 &middot; UEM JAIPUR &middot; 2026</p>' +
        '<p style="color:#555;font-size:11px;margin:8px 0 0;">This is an automated confirmation. Please do not reply.</p>' +
        '</td></tr>' +

        '</table></td></tr></table></body></html>';
}

// ─── Build HTML Welcome email ──────────────────────────────────────
function buildWelcomeHtml(toName) {
    return '<!DOCTYPE html><html><head><meta charset="UTF-8"></head>' +
        '<body style="margin:0;padding:0;background:#0d0020;font-family:Arial,sans-serif;">' +
        '<table width="100%" cellpadding="0" cellspacing="0" style="background:#0d0020;padding:40px 0;">' +
        '<tr><td align="center">' +
        '<table width="560" cellpadding="0" cellspacing="0" style="background:#12002e;border:1px solid rgba(212,165,32,0.3);border-radius:4px;overflow:hidden;max-width:100%;">' +

        // Header
        '<tr><td style="background:linear-gradient(135deg,#1a0040,#0d0020);padding:32px 36px 24px;border-bottom:1px solid rgba(212,165,32,0.2);">' +
        '<div style="font-family:Georgia,serif;font-size:26px;font-weight:bold;letter-spacing:4px;color:#fff;">AAROHAN</div>' +
        '<div style="font-size:11px;letter-spacing:3px;color:rgba(212,165,32,0.7);margin-top:4px;">1.0 &nbsp;&middot;&nbsp; THE BEGINNING OF A LEGACY</div>' +
        '</td></tr>' +

        // Body
        '<tr><td style="padding:32px 36px;">' +
        '<p style="color:#d4a520;font-size:13px;letter-spacing:2px;text-transform:uppercase;margin:0 0 8px;">Welcome to the Saga</p>' +
        '<h1 style="color:#fff;font-size:22px;margin:0 0 20px;font-family:Georgia,serif;">Welcome, ' + toName + '! &#127881;</h1>' +
        '<p style="color:#ccc;font-size:15px;line-height:1.7;margin:0 0 28px;">You have successfully signed in to the <strong style="color:#ffd700;">Aarohan 1.0</strong> portal.</p>' +
        '<p style="color:#ccc;font-size:15px;line-height:1.7;margin:0 0 28px;">You can now browse and register for events, form teams, and view your digital Gate Passes directly from your dashboard.</p>' +
        '<p style="color:#888;font-size:13px;line-height:1.7;">&#8505;&#65039; If you face any issues, feel free to reach out to the cultural committee.</p>' +
        '</td></tr>' +

        // Footer
        '<tr><td style="background:rgba(0,0,0,0.3);padding:20px 36px;border-top:1px solid rgba(212,165,32,0.1);text-align:center;">' +
        '<p style="color:rgba(212,165,32,0.5);font-size:11px;letter-spacing:2px;margin:0;">AAROHAN 1.0 &middot; UEM JAIPUR &middot; 2026</p>' +
        '<p style="color:#555;font-size:11px;margin:8px 0 0;">This is an automated confirmation. Please do not reply.</p>' +
        '</td></tr>' +

        '</table></td></tr></table></body></html>';
}
