from flask import Flask, render_template, request, redirect, url_for, session, flash

# Crear un nuevo posesionario
@app.route('/posesionarios/nuevo', methods=['GET', 'POST'])
def nuevo_posesionario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido_paterno = request.form['apellido_paterno']
        apellido_materno = request.form['apellido_materno']
        telefono = request.form['telefono']
        domicilio = request.form['domicilio']

        # Insertar en Supabase
        supabase.table('posesionarios').insert({
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "telefono": telefono,
            "domicilio": domicilio
        }).execute()
        flash('Posesionario registrado con éxito')
        return redirect(url_for('mostrar_posesionarios'))
    return render_template('nuevo_posesionario.html')

# Editar un posesionario
@app.route('/posesionarios/editar/<id>', methods=['GET', 'POST'])
def editar_posesionario(id):
    posesionario = supabase.table('posesionarios').select('*').eq('id', id).single().execute().data
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido_paterno = request.form['apellido_paterno']
        apellido_materno = request.form['apellido_materno']
        telefono = request.form['telefono']
        domicilio = request.form['domicilio']

        # Actualizar en Supabase
        supabase.table('posesionarios').update({
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "telefono": telefono,
            "domicilio": domicilio
        }).eq('id', id).execute()
        flash('Posesionario actualizado con éxito')
        return redirect(url_for('mostrar_posesionarios'))
    return render_template('editar_posesionario.html', posesionario=posesionario)

# Eliminar un posesionario
@app.route('/posesionarios/eliminar/<id>', methods=['POST'])
def eliminar_posesionario(id):
    supabase.table('posesionarios').delete().eq('id', id).execute()
    flash('Posesionario eliminado con éxito')
    return redirect(url_for('mostrar_posesionarios'))
