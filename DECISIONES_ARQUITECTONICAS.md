## Evaluación crítica

### 1. ¿Qué nueva dependencia hicieron explícita?

La dependencia principal que se hizo explícita es la de ServicioPedidos hacia el puerto InventarioPedidos. Antes, esa relación era implícita porque el constructor recibía un inventario sin indicar qué contrato debía cumplir.

También se hizo explícita la dependencia de las entradas hacia el formato externo de los pedidos. Ahora esta responsabilidad está aislada en la función mapear_pedido, evitando que el caso de uso conozca cómo llegan los datos desde cada canal.

---

### 2. ¿Qué dependencia invirtieron o aislaron?

Se eliminó la dependencia directa del núcleo con una implementación concreta del inventario. Ahora el núcleo depende del puerto InventarioPedidos, mientras que StockCloudInventario adapta las respuestas y métodos del proveedor externo al formato esperado por el sistema.

Además, los adapters de entrada quedaron separados del núcleo. El proceso batch no depende de HTTP y la API REST no tiene lógica de negocio propia, sino que utiliza el caso de uso mediante el contrato definido.

---

### 3. ¿Qué detalle externo quedó fuera del núcleo?

Los detalles externos que se aislaron fuera del núcleo son:

- El formato del diccionario recibido y los códigos de respuesta HTTP, que ahora se manejan desde entradas.py.
- Los estados y nombres de métodos propios de StockCloud, que son adaptados en inventario_stockcloud.py.
- Los detalles específicos del proveedor de pagos PayFast, que siguen manejándose en pagos.py.

---

### 4. ¿Qué cambio futuro quedó localizado?

Los posibles cambios futuros se pueden realizar en componentes específicos:

- Cambiar el proveedor de inventario solo requeriría modificar inventario_stockcloud.py y la función crear_inventario.
- Cambiar el formato de entrada de los pedidos modificaría únicamente la función mapear_pedido.
- Cambiar la implementación de la API REST por otro framework quedaría limitado a manejar_post_pedido.

---

### 5. ¿Qué complejidad adicional introdujo la solución?

La solución agregó algunos componentes adicionales:

- Una función de mapeo (mapear_pedido), dos adapters de entrada (manejar_post_pedido y procesar_lote) y un adapter de inventario (StockCloudInventario), junto con sus respectivas pruebas.
- La función procesar_pedido mantiene todavía una firma con 12 argumentos. Esto queda como una deuda técnica documentada, pero no se modifica porque no existe una necesidad que justifique cambiarlo.
- Existe un riesgo residual en el flujo de cobro y reserva. Actualmente procesar_pedido cobra antes de reservar el inventario. Si StockCloud falla durante la reserva, el cliente podría quedar cobrado sin tener la reserva confirmada. No se resolvió porque StockCloud no ofrece una operación para liberar o revertir unidades, y cambiar el orden requeriría una estrategia de compensación que la actividad no considera.
- Existe también un riesgo de reserva parcial. Si el pedido tiene varios productos, la reserva se realiza uno por uno. Si falla un producto después de reservar los anteriores, esas unidades quedan reservadas y el cliente ya fue cobrado. El puerto InventarioPedidos no tiene una operación de liberación y StockCloud tampoco la ofrece, por lo que esta solución no compensa ese error. El inventario local sí tiene devolver, pero no está incluido en el puerto, así que el núcleo no puede utilizarlo.
- El precio del producto llega desde el diccionario externo y se utiliza directamente para el cobro. Como no existe un catálogo de productos que valide este valor, queda como un riesgo pendiente de revisar.
- La anotación de tipo agregada en ServicioPedidos representa un cambio mínimo en el núcleo y no modifica su lógica de negocio

---

### 6. ¿Qué abstracción decidieron no crear y por qué?

Se decidió no crear algunas abstracciones adicionales porque no había una presión de cambio que las requiriera:

- Puerto de entrada: solo existe un caso de uso y cada adapter tiene un único punto de entrada. Crear un Protocol adicional agregaría una capa más sin resolver una necesidad actual.
- Command o DTO para los 12 argumentos: aunque podría mejorar la organización de los datos, implicaría modificar ServicioPedidos y sus pruebas existentes sin una necesidad concreta que lo requiera. El mapeo de entradas ya permite aislar el formato externo.
- Registro de servicios o Service Locator: no se implementó porque está prohibido por la consigna. En su lugar, crear_inventario recibe explícitamente la implementación que debe utilizar.
- Catálogo de productos: no se creó porque la actividad no plantea una presión de cambio relacionada con la validación de productos o precios. Por ahora, el precio recibido desde la entrada queda como un riesgo residual.