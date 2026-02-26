import os
import re

old_block = """        <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 3rem; padding-bottom: 2rem;">
            
            <div style="flex: 1; min-width: 250px;">
                <span class="footer-logo" style="font-family:'Cinzel',serif; font-size:1.5rem; font-weight:700; color:var(--gold, #d4a520);">AAROHAN 1.0</span>
                <div class="footer-ornament" style="margin: 0.5rem 0; color:var(--gold, #d4a520);">✦ ✦ ✦</div>
                <p style="font-style:italic; font-family:'Playfair Display',serif; color: rgba(212, 165, 32, 0.8);">The Beginning of a Legacy</p>
                <p style="margin-top:0.5rem; font-size:0.85rem; color: rgba(255,255,255,0.6);">University of Engineering &amp; Management, Jaipur</p>
            </div>
            
            <div style="flex: 1; min-width: 250px;">
                <h4 style="color: var(--gold, #d4a520); margin-bottom: 1.2rem; font-family: 'Cinzel', serif; letter-spacing: 0.1em; font-size: 1.1rem;">Contact Us</h4>
                <p style="margin-bottom: 0.8rem; font-size: 0.95rem;">
                    <strong style="color: rgba(255,255,255,0.9);">Mail:</strong><br> <a href="mailto:atranguemj@gmail.com" style="color: rgba(255,255,255,0.7); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--gold, #d4a520)'" onmouseout="this.style.color='rgba(255,255,255,0.7)'">atranguemj@gmail.com</a>
                </p>
                <div style="margin-bottom: 0.5rem; font-size: 0.95rem;">
                    <strong style="color: rgba(255,255,255,0.9);">Phone:</strong>
                    <div style="color: rgba(255,255,255,0.7); margin-top: 0.4rem; padding-left: 0.6rem; border-left: 2px solid rgba(212,165,32,0.3);">
                        <div style="margin-bottom: 0.3rem;">Soumik Chaudhuri: <a href="tel:9475858070" style="color: rgba(255,255,255,0.7); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--gold, #d4a520)'" onmouseout="this.style.color='rgba(255,255,255,0.7)'">9475858070</a></div>
                        <div>Arka Mahajan: <a href="tel:7047387377" style="color: rgba(255,255,255,0.7); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--gold, #d4a520)'" onmouseout="this.style.color='rgba(255,255,255,0.7)'">7047387377</a></div>
                    </div>
                </div>
            </div>

            <div style="flex: 1; min-width: 200px;">
                <h4 style="color: var(--gold, #d4a520); margin-bottom: 1.2rem; font-family: 'Cinzel', serif; letter-spacing: 0.1em; font-size: 1.1rem;">Follow Us</h4>
                <div style="display: flex; gap: 1.2rem; align-items: center;">
                    <a href="https://www.instagram.com/atrang_uemj_/" target="_blank" style="color: rgba(255,255,255,0.7); transition: color 0.3s, transform 0.3s; display: inline-block; transform-origin: center;" onmouseover="this.style.color='var(--gold, #d4a520)'; this.style.transform='scale(1.1) translateY(-2px)'" onmouseout="this.style.color='rgba(255,255,255,0.7)'; this.style.transform='scale(1) translateY(0)'" title="Instagram">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                            <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                        </svg>
                    </a>
                    <a href="https://www.youtube.com/channel/UC_F8-WiuRnMFBxbIEmr9UDg" target="_blank" style="color: rgba(255,255,255,0.7); transition: color 0.3s, transform 0.3s; display: inline-block; transform-origin: center;" onmouseover="this.style.color='var(--gold, #d4a520)'; this.style.transform='scale(1.1) translateY(-2px)'" onmouseout="this.style.color='rgba(255,255,255,0.7)'; this.style.transform='scale(1) translateY(0)'" title="YouTube">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25z"></path>
                            <polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon>
                        </svg>
                    </a>
                </div>
            </div>
            
        </div>"""

new_block = """        <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; justify-content: center; gap: 3rem; padding-bottom: 2rem;">
            
            <div style="flex: 1; min-width: 250px; text-align: center; border-right: 1px solid rgba(212,165,32,0.2); padding-right: 2rem;">
                <span class="footer-logo" style="font-family:'Cinzel',serif; font-size:1.5rem; font-weight:700; color:var(--gold, #d4a520);">AAROHAN 1.0</span>
                <div class="footer-ornament" style="margin: 0.5rem 0; color:var(--gold, #d4a520);">✦ ✦ ✦</div>
                <p style="font-style:italic; font-family:'Playfair Display',serif; color: rgba(212, 165, 32, 0.8);">The Beginning of a Legacy</p>
                <p style="margin-top:0.5rem; font-size:0.85rem; color: rgba(255,255,255,0.6);">University of Engineering &amp; Management, Jaipur</p>
            </div>
            
            <div style="flex: 1; min-width: 250px; text-align: center;">
                <h4 style="color: var(--gold, #d4a520); margin-bottom: 1.2rem; font-family: 'Cinzel', serif; letter-spacing: 0.1em; font-size: 1.1rem; text-transform: uppercase;">Contact Us</h4>
                <p style="margin-bottom: 0.8rem; font-size: 0.95rem;">
                    <strong style="color: rgba(255,255,255,0.9);">Mail:</strong><br> <a href="mailto:atranguemj@gmail.com" style="color: rgba(255,255,255,0.7); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--gold, #d4a520)'" onmouseout="this.style.color='rgba(255,255,255,0.7)'">atranguemj@gmail.com</a>
                </p>
                <div style="margin-bottom: 0.5rem; font-size: 0.95rem;">
                    <strong style="color: rgba(255,255,255,0.9);">Phone:</strong>
                    <div style="color: rgba(255,255,255,0.7); margin-top: 0.4rem;">
                        <div style="margin-bottom: 0.3rem;">Soumik Chaudhuri: <a href="tel:9475858070" style="color: rgba(255,255,255,0.7); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--gold, #d4a520)'" onmouseout="this.style.color='rgba(255,255,255,0.7)'">9475858070</a></div>
                        <div>Arka Mahajan: <a href="tel:7047387377" style="color: rgba(255,255,255,0.7); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--gold, #d4a520)'" onmouseout="this.style.color='rgba(255,255,255,0.7)'">7047387377</a></div>
                    </div>
                </div>
            </div>

            <div style="flex: 1; min-width: 200px; text-align: center;">
                <h4 style="color: var(--gold, #d4a520); margin-bottom: 1.2rem; font-family: 'Cinzel', serif; letter-spacing: 0.1em; font-size: 1.1rem; text-transform: uppercase;">Follow Us</h4>
                <div style="display: flex; gap: 1.2rem; align-items: center; justify-content: center;">
                    <a href="https://www.instagram.com/atrang_uemj_/" target="_blank" style="color: rgba(255,255,255,0.7); transition: color 0.3s, transform 0.3s; display: inline-block; transform-origin: center;" onmouseover="this.style.color='var(--gold, #d4a520)'; this.style.transform='scale(1.1) translateY(-2px)'" onmouseout="this.style.color='rgba(255,255,255,0.7)'; this.style.transform='scale(1) translateY(0)'" title="Instagram">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                            <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                        </svg>
                    </a>
                    <a href="https://www.youtube.com/channel/UC_F8-WiuRnMFBxbIEmr9UDg" target="_blank" style="color: rgba(255,255,255,0.7); transition: color 0.3s, transform 0.3s; display: inline-block; transform-origin: center;" onmouseover="this.style.color='var(--gold, #d4a520)'; this.style.transform='scale(1.1) translateY(-2px)'" onmouseout="this.style.color='rgba(255,255,255,0.7)'; this.style.transform='scale(1) translateY(0)'" title="YouTube">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25z"></path>
                            <polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon>
                        </svg>
                    </a>
                </div>
            </div>
            
        </div>"""

directory = r"e:\AArohan"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_block in content:
            new_content = content.replace(old_block, new_block)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Skipped {filename} (block not found)")
