import re
import os

files = [
    r"c:\Users\Sayed\.gemini\antigravity\scratch\health-security-screen\index.html",
    r"c:\Users\Sayed\.gemini\antigravity\scratch\health-security-screen\account.html",
    r"c:\Users\Sayed\.gemini\antigravity\scratch\health-security-screen\security.html",
    r"c:\Users\Sayed\.gemini\antigravity\scratch\health-security-screen\privacy-policy.html"
]

def px_to_rem(match):
    prop = match.group(1)
    val = match.group(2)
    if val == "0" or val == "1":
        return match.group(0)
    
    vals = val.split()
    new_vals = []
    for v in vals:
        if v.endswith("px"):
            try:
                num = float(v.replace("px", ""))
                if num > 2:
                    new_vals.append(f"{num/16:g}rem")
                else:
                    new_vals.append(v)
            except ValueError:
                new_vals.append(v)
        else:
            new_vals.append(v)
            
    return f"{prop}: {' '.join(new_vals)};"

prop_pattern = re.compile(r'(font-size|margin(?:-[a-z]+)?|padding(?:-[a-z]+)?)\s*:\s*([^;]+);')

media_query = """
        /* Desktop Mockup View */
        @media (min-width: 481px) {
            body {
                padding: 1.25rem;
            }
            .mobile-container {
                height: 896px;
                max-height: 90vh;
                min-height: auto;
                box-shadow: var(--shadow-md);
                border-radius: 36px;
                border: 10px solid #1a202c;
                margin: auto;
            }
        }
"""

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    body_pattern = re.compile(r'body\s*\{[^}]*display:\s*flex;[^}]*\}', re.DOTALL)
    new_body = """body {
            font-family: 'Cairo', system-ui, -apple-system, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 0;
            margin: 0;
            overflow-x: hidden;
        }"""
    content = body_pattern.sub(new_body, content)
        
    mobile_container_pattern = re.compile(r'\.mobile-container\s*\{[^}]*\}', re.DOTALL)
    new_container = """.mobile-container {
            width: 100%;
            max-width: 480px; 
            min-height: 100vh; 
            background-color: var(--bg-color);
            position: relative;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            margin: 0 auto;
        }"""
    content = mobile_container_pattern.sub(new_container, content)
        
    if "/* Desktop Mockup View */" not in content:
        content = content.replace("</style>", media_query + "\n    </style>")
        
    content = prop_pattern.sub(px_to_rem, content)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully processed {len(files)} files.")
