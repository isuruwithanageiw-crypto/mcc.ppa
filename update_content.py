import os

directory = r"e:\mcc alumni"

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Specifically handle the logo replacement before we change MCCAA
    logo_icon = '<i class="fa-solid fa-graduation-cap text-2xl text-white"></i>'
    logo_img = '<img src="images/logo.jpg" alt="Logo" class="w-full h-full object-cover">'
    content = content.replace(logo_icon, logo_img)
    
    # Also we should update the logo container to handle overflow-hidden
    logo_container = '<div class="w-12 h-12 bg-gradient-to-br from-accent-blue to-accent-purple rounded-xl flex items-center justify-center shadow-lg shadow-blue-500/20">'
    logo_container_new = '<div class="w-12 h-12 bg-gradient-to-br from-accent-blue to-accent-purple rounded-xl flex items-center justify-center shadow-lg shadow-blue-500/20 overflow-hidden">'
    content = content.replace(logo_container, logo_container_new)

    # Generic replaces - careful with casing
    content = content.replace("MCCAA", "MCCPPA")
    content = content.replace("Alumni Association", "Past Pupils Association")
    content = content.replace("alumni association", "past pupils association")
    
    # Protect css class names or URLs if any
    content = content.replace("mccaalumni.lk", "mccppa.lk") # Fix emails BEFORE general alumni replace
    
    content = content.replace("Alumni Network", "Past Pupils Network")
    content = content.replace("Alumni Application", "Past Pupils Application")
    content = content.replace("Alumni", "Past Pupils")
    content = content.replace("alumni", "past pupils")
    
    # Specific image replacement (School)
    school_old = 'https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1920&auto=format&fit=crop'
    school_new = 'images/school.jpg'
    content = content.replace(school_old, school_new)
    
    school_old_2 = 'https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=1920&auto=format&fit=crop'
    content = content.replace(school_old_2, school_new)
    
    # Board members
    content = content.replace("Dr. Ajith Silva", "Mr. KHP Kumarasiri")
    content = content.replace("Dr. S. K. Perera", "Mr. Saman Kuruppuarachchi")
    content = content.replace("Mr. Ruwan Fernando", "Mr. Nimal Samarawickrama")
    
    # Replace Secretary with Chief Secretary
    content = content.replace('<div class="text-accent-purple text-sm font-semibold uppercase tracking-wider mb-4">Secretary</div>', '<div class="text-accent-purple text-sm font-semibold uppercase tracking-wider mb-4">Chief Secretary</div>')
    
    # Contact numbers
    content = content.replace("+94 41 222 3333", "+94412224301")
    content = content.replace("+94 77 123 4567", "+94714773567")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        replace_in_file(os.path.join(directory, filename))

print("Replacements done.")
