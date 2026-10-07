# Publicar y entregar

El código funciona únicamente con Python estándar. El repositorio local está
en la rama `main`, con los commits preparados. Git ya está instalado.
GitHub CLI se descargó de su distribución oficial en `tmp/github-cli/bin/gh.exe`
(herramienta local excluida del repositorio). Falta autorizar la cuenta de GitHub
y publicar el repositorio.

1. Desde PowerShell, abrir el proyecto y usar GitHub CLI local:

   ```powershell
   cd C:\Users\usuario\Documents\poo\tarea-unidad4-poo
   $env:GH_CONFIG_DIR = Join-Path (Get-Location) 'tmp\github-config'
   $gh = '.\tmp\github-cli\bin\gh.exe'
   ```

2. Iniciar sesión y publicar:

   ```powershell
   & $gh auth login --hostname github.com --git-protocol https --web
   git remote -v
   & $gh repo create tarea-unidad4-poo-python --public --source=. --remote=origin --push
   & $gh repo view --json url --jq .url
   ```

   El comando de creación se usa solo si todavía no existe `origin` ni un
   repositorio con ese nombre. No eliminar repositorios ni usar `--force`.
   Si el repositorio ya existe en GitHub, agregar su URL con
   `git remote add origin URL_DEL_REPOSITORIO` y ejecutar `git push -u origin main`.

3. Pegar el enlace real al inicio de `Evidencia_Unidad_IV.docx` y guardar también
   la versión `.doc` desde Word (Documento de Word 97-2003), conservando las capturas.
4. Guardar el cambio en Git y subirlo:

   ```powershell
   git add Evidencia_Unidad_IV.doc Evidencia_Unidad_IV.docx
   git commit -m "docs: agregar enlace al repositorio publicado"
   git push
   ```

5. Subir `Evidencia_Unidad_IV.doc` a Canvas. La captura de la tarea indica
   que el tipo de archivo admitido es `doc`.
