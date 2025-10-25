

CREATE TABLE categoria (
    id_categoria   int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre         varchar(150) NOT NULL
);

CREATE TABLE marca (
    id_marca       int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre         varchar(150) NOT NULL
);

CREATE TABLE modelo (
    id_modelo      int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre         varchar(150) NOT NULL
);

CREATE TABLE producto (
    id_producto    int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre         varchar(200) NOT NULL,
    descripcion    text,
    precio         numeric(12,2) NOT NULL DEFAULT 0.00,
    stock          integer NOT NULL DEFAULT 0,
    id_categoria   int NOT NULL REFERENCES categoria(id_categoria),
    id_marca       int NOT NULL REFERENCES marca(id_marca),
    id_modelo      int REFERENCES modelo(id_modelo),
    created_at     timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX idx_producto_categoria ON producto(id_categoria);
CREATE INDEX idx_producto_marca ON producto(id_marca);


----Daniel estas son las funciones para poder hacer el CRUD melo----

--- estas son las de la tabla PRODUCTO

---PUT
create or replace function spaIngresarProducto(
    p_nombre text,
    p_descripcion text,
    p_precio numeric,
    p_stock integer,
    p_idcategoria integer,
    p_idmarca integer,
    p_idmodelo integer
) returns integer as $$
declare
    nuevo_id integer;
begin
    insert into producto (nombre, descripcion, precio, stock, id_categoria, id_marca, id_modelo)
    values (p_nombre, p_descripcion, p_precio, p_stock, p_idcategoria, p_idmarca, p_idmodelo)
    returning id_producto into nuevo_id;
    return nuevo_id;
end;
$$ language plpgsql;

--- GET   spaConsultarProducto() es el nombre de la funcione ome Follilo

create or replace function spaConsultarProducto()
returns table(
    id_producto int,
    nombre text,
    descripcion text,
    precio numeric,
    stock int,
    id_categoria int,
    id_marca int,
    id_modelo int,
    created_at timestamptz
) as $$
begin
    return query
    select id_producto, nombre, descripcion, precio, stock, id_categoria, id_marca, id_modelo, created_at
    from producto
    order by id_producto;
end;
$$ language plpgsql;

--- GET pero por ID

create or replace function spaConsultarProductoPorId(p_id integer)
returns table(
    id_producto int,
    nombre text,
    descripcion text,
    precio numeric,
    stock int,
    id_categoria int,
    id_marca int,
    id_modelo int,
    created_at timestamptz
) as $$
begin
    return query
    select id_producto, nombre, descripcion, precio, stock, id_categoria, id_marca, id_modelo, created_at
    from producto
    where id_producto = p_id;
end;
$$ language plpgsql;

--- UPDATE (PUT)este si me quedo como raro

create or replace function spaActualizarProducto(
    p_id integer,
    p_nombre text,
    p_descripcion text,
    p_precio numeric,
    p_stock integer,
    p_idcategoria integer,
    p_idmarca integer,
    p_idmodelo integer
) returns integer as $$
declare
    rows_updated integer;
begin
    update producto
    set nombre = p_nombre,
        descripcion = p_descripcion,
        precio = p_precio,
        stock = p_stock,
        id_categoria = p_idcategoria,
        id_marca = p_idmarca,
        id_modelo = p_idmodelo
    where id_producto = p_id;

    get diagnostics rows_updated = row_count;
    return rows_updated;
end;
$$ language plpgsql;

--- deLETE

create or replace function spaEliminarProducto(p_id integer)
returns integer as $$
declare
    rows_deleted integer;
begin
    delete from producto where id_producto = p_id;
    get diagnostics rows_deleted = row_count;
    return rows_deleted; 
end;
$$ language plpgsql;