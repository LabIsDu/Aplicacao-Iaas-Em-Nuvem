import sqlite3

def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clinica (
        clinica_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cnpj TEXT NOT NULL UNIQUE,
        razao_social TEXT NOT NULL,
        nome_fantasia TEXT NOT NULL,
        endereco TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL,
        registro_conselho INTEGER NOT NULL,
        plano_id INTEGER,
        FOREIGN KEY (plano_id) REFERENCES plano(plano_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS paciente (
        paciente_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf TEXT NOT NULL,
        nome_paciente TEXT NOT NULL,
        plano_id INTEGER,
        FOREIGN KEY (plano_id) REFERENCES plano(plano_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dentista (
        dentista_id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_cro TEXT NOT NULL UNIQUE,
        nome_dentista TEXT NOT NULL,
        especializacao TEXT,
        certificacao TEXT,
        email TEXT NOT NULL UNIQUE,
        telefone TEXT NOT NULL,
        clinica_id INTEGER NOT NULL,
        consultorio_id INTEGER NOT NULL,
        FOREIGN KEY (clinica_id) REFERENCES clinica(clinica_id),
        FOREIGN KEY (consultorio_id) REFERENCES consultorio(consultorio_id)
    )
    ''')

    cursor.execute("SELECT COUNT(*) FROM clinica")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO clinica (cnpj, razao_social, nome_fantasia, endereco, telefone, email, registro_conselho) VALUES ('12345678000195', 'Clínica Saúde Ltda', 'Saúde Fácil', 'Rua das Flores, 123', '11987654321', 'contato@saudefacil.com.br', 12345)")
    
    cursor.execute("SELECT COUNT(*) FROM paciente")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO paciente (cpf, nome_paciente, plano_id) VALUES ('12345678901', 'João da Silva', 1)")
    
    cursor.execute("SELECT COUNT(*) FROM dentista")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO dentista (numero_cro, nome_dentista, especializacao, certificacao, email, telefone, clinica_id, consultorio_id) VALUES ('123456', 'Dr. Pedro Lima', 'Ortodontia', 'Certificado ABC', 'pedro.lima@saude.com', '11987654322', 1, 1)")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
