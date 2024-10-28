class Editorial:
    def __init__(self, id, cif, razon,direccion,web,correo,tlf):
        self.id = id
        self.cif = cif
        self.razon = razon
        self.direccion = direccion
        self.web = web
        self.correo = correo
        self.tlf = tlf

    def __str__(self):
        return (f"ID: {self.id} CIF: {self.cif} Razón social: {self.razon} Dirección: {self.direccion} Web: {self.web} "
                f"Correo: {self.correo} Teléfono: {self.tlf}")
        
    def serialize(self):
        return {"id": self.id, "cif": self.cif, "razon": self.razon, "direccion": self.direccion, "web": self.web, 
                "correo": self.correo, "tlf": self.tlf}