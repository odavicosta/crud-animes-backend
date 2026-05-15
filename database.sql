CREATE DATABASE black_clover;
USE black_clover;

CREATE TABLE locais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(20) NOT NULL
);

CREATE TABLE racas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(20) NOT NULL
);

CREATE TABLE espiritos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(20) NOT NULL,
    elemento VARCHAR(20) NOT NULL
);

CREATE TABLE esquadroes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    id_local INT NOT NULL,
    FOREIGN KEY (id_local) REFERENCES locais(id)
);

CREATE TABLE personagens (
id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    tipo_magia VARCHAR(30) NOT NULL,
    
    id_esquadrao INT, 
    id_espirito INT,  
    id_raca INT NOT NULL,
    id_raca_secundaria INT,
    id_local_origem INT NOT NULL,
    
    eh_portador_atual BOOLEAN DEFAULT FALSE,
    eh_nobre BOOLEAN DEFAULT FALSE,
    eh_portador_demoniaco BOOLEAN DEFAULT FALSE,
    
    FOREIGN KEY (id_esquadrao) REFERENCES esquadroes(id),
    FOREIGN KEY (id_espirito) REFERENCES espiritos(id),
    FOREIGN KEY (id_raca) REFERENCES racas(id),
    FOREIGN KEY (id_raca_secundaria) REFERENCES racas(id),
    FOREIGN KEY (id_local_origem) REFERENCES locais(id)
);