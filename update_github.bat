@echo off
echo Updating GitHub repository...
git add .
git commit -m "Fix Supabase image URL handling for consistent display across all pages"
git push origin main
echo Done!
pause