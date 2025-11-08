
#weAPITIENDAELECTRO

from fastapi import FastAPI
from domain.geografia.pais.paismodel import PaisModel
from domain.geografia.departamento.departamentomodel import DepartamentoModel
from domain.geografia.ciudad.ciudadmodel import CiudadModel
from domain.producto.producto.ProductoModel import ProductoModel
from domain.organizacion.sede.sedemodel import SedeModel

from infraestructure.geografia.pais.paisinfrastructure import PaisInfrastructure
from infraestructure.geografia.departamento.departamentoinfrastructure import DepartamentoInfrastructure
from infraestructure.geografia.ciudad.ciudadinfrastructure import CiudadInfrastructure
from infraestructure.organizacion.sede.sedeinfrastructure import SedeInfrastructure
from infraestructure.producto.producto.productoinfrastructure import ProductoInfrastructure


##############################################



app: FastAPI = FastAPI(

    title="Tienda Electro",
    description="API REST de una tienda de electrodomésticos",

)








from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost:3000"]  # Aquí pones la URL donde corre tu React

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




































###########################################

#geografia.pais

#CONMSULTAR PAIS
@app.get(
    "/paisget",
    summary="Metodo Pais Get",
    description ="Operacion Pais Get",
    tags=["geografia.pais"]
)
async def consultar_pais():
    return PaisInfrastructure.consultar_pais()

#CONSULTAR PAIS POR ID
@app.get(
    "/paisgetID",
    summary="Metodo Pais Get",
    description ="Operacion Pais Get",
    tags=["geografia.pais"]
)
async def consultar_pais_por_id(idpais: str):
    return PaisInfrastructure.consultar_pais_por_id(idpais)

#INSERTAR PAIS
@app.post(
        "/paispost",
        summary="Metodo Pais Post",
        description="Operacion Pais Post",
        tags=["geografia.pais"]
)
async def ingresar_pais(pais: PaisModel):
    return PaisInfrastructure.ingresar_pais(pais)

#MODIFICAR PAIS
@app.put(
        "/paisput",
        summary="Metodo Pais Put",
        description="Operacion Pais Put",
        tags=["geografia.pais"]
)
async def modificar_pais(idpais: str, pais: PaisModel):
    pais.idpais = idpais
    return PaisInfrastructure.modificar_pais(pais)


@app.delete(
        "/paisdelete",
        summary="Metodo Pais Delete",
        description="Operacion Pais Delete",
        tags=["geografia.pais"]
)
async def eliminar_pais(idpais: str):
    return PaisInfrastructure.eliminar_pais(idpais)




#geografia.departamento
#CONSULTAR DEPARTAMENTO
@app.get(
    "/departamentoget",
    summary="Metodo Departamento Get",
    description ="Operacion Departamento Get",
    tags=["geografia.departamento"]
)
async def consultar_departamento():
    return DepartamentoInfrastructure.consultar_departamento()

#CONMSULTAR DEPARTAMENTO POR ID
@app.get(
    "/departamentogetID",
    summary="Metodo Departamento Get",
    description ="Operacion Departamento Get",
    tags=["geografia.departamento"]
)
async def consultar_departamento_por_id(iddepartamento: str):
    return DepartamentoInfrastructure.consultar_departamento_por_id(iddepartamento)

#INGRESAR DEPARTAMENTO
@app.post(
        "/departamentopost",

        summary="Metodo Departamento Post",
        description="Operacion Departamento Post",
        tags=["geografia.departamento"]
)
async def ingresar_departamento(dep: DepartamentoModel):
    return DepartamentoInfrastructure.ingresar_departamento(dep)

#MODIFICAR DEPARTAMENTO
@app.put(
        "/departamentoput",
        summary="Metodo Departamento Put",
        description="Operacion Departamento Put",
        tags=["geografia.departamento"]
)
async def modificar_departamento(iddepartamento: str, dep: DepartamentoModel):
    dep.iddepartamento = iddepartamento
    return DepartamentoInfrastructure.modificar_departamento(dep)

#ELIMINAR DEPARTAMENTO
@app.delete(
        "/departamentodelete",  
        summary="Metodo Departamento Delete",
        description="Operacion Departamento Delete",
        tags=["geografia.departamento"]
)
async def eliminar_departamento(iddepartamento: str):
    return DepartamentoInfrastructure.eliminar_departamento(iddepartamento)


#################################

#geografia.ciudad
#CONSULTAR CIUDAD
@app.get(
    "/ciudadget",
    summary="Metodo Ciudad Get",
    description ="Operacion Ciudad Get",
    tags=["geografia.ciudad"]
)
async def consultar_ciudad():
    return CiudadInfrastructure.consultar_ciudad()

#CONSULTAR CIUIDAD POR ID
@app.get(
    "/ciudadgetID",
    summary="Metodo Ciudad Get",
    description ="Operacion Ciudad Get",
    tags=["geografia.ciudad"]
)
async def consultar_ciudad_por_id(idciudad: str):
    return CiudadInfrastructure.consultar_ciudad_por_id(idciudad)


#INFRESAR CIUDAD
@app.post(
        "/ciudadpost",
        summary="Metodo Ciudad Post",
        description="Operacion Ciudad Post",
        tags=["geografia.ciudad"]
)
async def ingresar_ciudad(ciudad: CiudadModel):
    return CiudadInfrastructure.ingresar_ciudad(ciudad)

#MODIFICAR CIUDAD
@app.put(
        "/ciudadput",
        summary="Metodo Ciudad Put",
        description="Operacion Ciudad Put",
        tags=["geografia.ciudad"]
)
async def modificar_ciudad(idciudad: str, ciudad: CiudadModel):
    ciudad.idciudad = idciudad
    return CiudadInfrastructure.modificar_ciudad(ciudad)
#ELIMINAR CIUDAD
@app.delete(
        "/ciudaddelete",
        summary="Metodo Ciudad Delete",
        description="Operacion Ciudad Delete",
        tags=["geografia.ciudad"]
)
async def eliminar_ciudad(idciudad: str):
    return CiudadInfrastructure.eliminar_ciudad(idciudad)

###########################################

#organizacion.sede
#CONSULTAR SEDE
@app.get(
    "/sedget",
    summary="Método Sede Get",
    description="Operación Sede Get",
    tags=["organizacion.sede"]
)
async def consultar_sede():
    return SedeInfrastructure.consultar_sede()
#CONSULTAR SEDE POR ID
@app.get(
    "/sedgetID",
    summary="Método Sede Get",
    description="Operación Sede Get",
    tags=["organizacion.sede"]
)
async def consultar_sede_por_id(idsede: str):
    return SedeInfrastructure.consultar_sede_por_id(idsede)
@app.post(
    "/sedpost",

    summary="Método Sede Post",
    description="Operación Sede Post",
    tags=["organizacion.sede"]
)
async def ingresar_sede(sede: SedeModel):
    return SedeInfrastructure.ingresar_sede(sede)

#MODIFICAR SEDE
@app.put(
    "/sedput",

    summary="Método Sede Put",
    description="Operación Sede Put",
    tags=["organizacion.sede"]
)
async def modificar_sede(idsede: str, sede: SedeModel):
    sede.idsede = idsede
    return SedeInfrastructure.modificar_sede(sede)
#ELIMINAR SEDE
@app.delete(
    "/seddelete",
    summary="Método Sede Delete",
    description="Operación Sede Delete",
    tags=["organizacion.sede"]
)
async def eliminar_sede(idsede: str):
    return SedeInfrastructure.eliminar_sede(idsede)
###########################################

#producto.producto
#CONSULTAR PRODUCTO
@app.get(
    "/productoget",
    summary="Método Modelo Get",
    description="Operación Modelo Get",
    tags=["producto.producto"]
)
async def consultar_producto():
    return ProductoInfrastructure.consultar_producto()

#CONSULTAR PRODUCTO POR ID
@app.get(
    "/productogetID",
    summary="Método producto Get",
    description="Operación productoGet",
    tags=["producto.producto"]
)
async def consultar_producto_por_id(idproducto: str):
    return ProductoInfrastructure.consultar_producto_por_id(idproducto)

#INSERTAR PRODUCTO
@app.post(
    "/productopost",
    summary="Método producto Post",
    description="Operación producto Post",
    tags=["producto.producto"]
)
async def ingresar_producto(prod: ProductoModel):
    return ProductoInfrastructure.ingresar_producto(prod)

#MODIFICAR PRODDUCTO
@app.put(
    "/productoput",       
    summary="Método producto Put",
    description="Operación producto Put",
    tags=["producto.producto"]
)
async def modificar_producto(idproducto: str, prod: ProductoModel):
    prod.idproducto = idproducto
    return ProductoInfrastructure.modificar_producto(prod)

#ELIMINAR PRODUCTO
@app.delete(
    "/productodelete",        
    summary="Método productoDelete",
    description="Operación producto Delete",
    tags=["producto.producto"]
)
async def eliminar_producto(idproducto: str):
    return ProductoInfrastructure.eliminar_producto(idproducto)








































