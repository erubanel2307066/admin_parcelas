from flask import render_template, request, redirect, url_for, current_app, flash
import os

def upload_file_to_supabase(file):
    supabase = current_app.supabase
    bucket_name = "parcelas-pdfs"
    file_path = f"uploads/{file.filename}"
    
    # Guardar localmente antes de subir
    file.save(file_path)
    
    # Subir archivo a Supabase Storage
    response = supabase.storage.from_(bucket_name).upload(file_path, file_path)

    if response.get('error'):
        flash("Error al subir el archivo.")
        return None

    # Obtener URL del archivo en Supabase
    url = supabase.storage.from_(bucket_name).get_public_url(file_path).get('publicURL')
    return url

@current_app.route('/')
def index():
    supabase = current_app.supabase
    data = supabase.table('parcelas').select('*').execute()
    parcelas = data.get('data', [])
    return render_template('index.html', parcelas=parcelas)

@current_app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        folio = request.form['folio']
        propietario = request.form['propietario']
        medida = request.form['medida']
        colindancias = request.form['colindancias']
        file = request.files['documento']
        file_url = upload_file_to_supabase(file)
        
        if file_url:
            supabase = current_app.supabase
            supabase.table('parcelas').insert({
                "folio": folio,
                "propietario": propietario,
                "medida": medida,
                "colindancias": colindancias,
                "documento": file_url
            }).execute()
            flash('Parcela registrada con éxito.')
            return redirect(url_for('index'))
        else:
            flash('Error al registrar la parcela.')

    return render_template('registro_parcela.html')
