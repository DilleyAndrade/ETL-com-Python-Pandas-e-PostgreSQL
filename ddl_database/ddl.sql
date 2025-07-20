CREATE TABLE ITENS_PEDIDOS(
	id_item INT PRIMARY KEY,
	id_pedido INT,
	id_produto INT,
	quantidade INT,
	preco_unitario REAL,
	CONSTRAINT FK_id_pedido FOREIGN KEY(id_pedido) REFERENCES PEDIDOS(id_pedido) 
);

CREATE TABLE PEDIDOS(
	id_pedido INT PRIMARY KEY,
	data_compra DATE,
	id_cliente INT,
	valor_total REAL,
	status_pedido VARCHAR(50)
);