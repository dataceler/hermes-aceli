Default Hermes Google OAuth covers Calendar, Drive, Sheets, Docs, read-only Gmail and read-only YouTube; Gmail send/modify, Contacts and YouTube write are excluded.
§
User operates two Hermes instances on a Hostinger VPS: one in Docker and one installed directly on the host. The host dashboard listens on VPS loopback port 9119 and is accessed from the user's Mac through an SSH tunnel using local port 4861. The Docker instance is separate.
§
Discord allows all users; server channels still require an @Sansão mention by default.
§
Granola's read-only API is configured in the default Hermes profile via GRANOLA_API_KEY and validated against the official notes endpoint.
§
Hostinger API access for the Dataceler account is configured in the default Hermes profile via HOSTINGER_API_TOKEN and validated with the read-only VPS inventory endpoint.
§
Coolify API access for Dataceler is configured in the default Hermes profile with an HTTPS base URL and token stored in .env; authentication was validated with the read-only teams endpoint.
§
Official Canva and vidIQ MCPs are OAuth-configured in default Hermes. vidIQ uses 31/53 selected tools with account mutation and media/voice generation disabled; free read-only balance/channel calls were validated. Canva CLI 2.8.1 is installed.
§
Dataceler LinkedIn content is authored by João Cordeiro at https://www.linkedin.com/in/joaocordeiroia/. The target audience includes SME owners and managers, non-technical people, and IT professionals who want to learn about AI. The editorial tone is executive, and the primary CTA should invite comments.
§
The preferred Aceli brand avatar is a cute, friendly abstract virtual-pet mascot (Tamagotchi-like but original), not an animal, human, robot, frightening figure, or ornate/gamer aesthetic. It should use Dataceler's charcoal, cream, and bronze palette with the official Dataceler symbol in black.
§
Dataceler LinkedIn posts require an image and default to infographics. LinkedIn infographics are rendered deterministically with Python/Pillow, DejaVu Sans/Mono, and code-positioned text, shapes, matrices, arrows, colors, and logo; prioritize analytical depth over sales copy.