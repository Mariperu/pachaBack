from orator.migrations import Migration


class CreateTables(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cliente_tables') as table:
            table.increments('id_cliente')
            table.string('nombre', 50)
            table.string('direccion', 100)
            table.string('telefono', 20)

        with self.schema.create('producto_tables') as table:
            table.increments('id_producto')
            table.string('nombre', 50)
            table.decimal('precio', 10, 2)
            table.integer('stock')

        with self.schema.create('venta_tables') as table:
            table.increments('id_venta')
            table.integer('id_cliente').unsigned()
            table.foreign('id_cliente').references('id_cliente').on('cliente_tables')
            table.date('fecha_venta')
            table.decimal('monto_total', 10, 2)

        with self.schema.create('detalle_venta_tables') as table:
            table.increments('id_detalle')
            table.integer('id_venta').unsigned()
            table.foreign('id_venta').references('id_venta').on('venta_tables')
            table.integer('id_producto').unsigned()
            table.foreign('id_producto').references('id_producto').on('producto_tables')
            table.integer('cantidad')
            table.decimal('subtotal', 10, 2)

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('detalle_venta_tables')
        self.schema.drop('venta_tables')
        self.schema.drop('producto_tables')
        self.schema.drop('cliente_tables')
