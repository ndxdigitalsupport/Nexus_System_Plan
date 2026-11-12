import zipfile
import os

files_to_pack = [
    "NEXUS_ECOSYSTEM_AUDIT_AND_BRAND_GUIDEBOOK.docx",
    "nexus_portfolio_dashboard.html",
    "nexus_executive_slides.html",
    "nexus_ui_design_system_and_prototypes.html",
    "MARKETING_MATERIALS_AND_BATTLECARDS.md",
    "NEXUS_TECHNICAL_DOCUMENTATION.md",
    "NEXUS_BRANDED_GUIDEBOOK_AND_AUDIT.md",
    "EXECUTIVE_DECISION_CHEATSHEET.md",
    "DNS_AND_INFRASTRUCTURE_MIGRATION_GUIDE.md",
    "Q4_MARKETING_LAUNCH_CALENDAR.md",
    "nexus-global-bar.js",
    "nexus-tokens.css",
    "DIGITAL_ASSET_MANIFEST.json"
]

zip_filename = "Nexus_Executive_Deliverable_Pack.zip"

print(f"Creating {zip_filename}...")
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for filename in files_to_pack:
        if os.path.exists(filename):
            zipf.write(filename, arcname=filename)
            print(f"  + Added: {filename}")
        else:
            print(f"  ! Warning: {filename} not found.")

    # Pack sites directory recursively
    if os.path.exists("sites"):
        for root, dirs, files in os.walk("sites"):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, ".")
                zipf.write(filepath, arcname=arcname)
                print(f"  + Added: {arcname}")

size_kb = os.path.getsize(zip_filename) / 1024
print(f"Successfully packaged {zip_filename} ({size_kb:.1f} KB)")
