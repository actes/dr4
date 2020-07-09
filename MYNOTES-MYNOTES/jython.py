return u' '  +  unichr( int(value,16) )

Reuse	This project	jython:	return type(cell)

Reuse	This project	jython:	return dir(value)

return dir()
1.	to	[ "cell", "cells", "row", "rowIndex", "value" ]

return dir(cells)
1.	to	[ "__class__", "__delattr__", "__doc__", "__ensure_finalizer__", "__finditem__", "__format__", "__getattribute__", "__hash__", "__init__", "__new__", "__reduce__", "__reduce_ex__", "__repr__", "__setattr__", "__str__", "__subclasshook__", "_obj" ]

return dir(cell._obj)
1.	to	[ "__class__", "__copy__", "__deepcopy__", "__delattr__", "__doc__", "__ensure_finalizer__", "__eq__", "__format__", "__getattribute__", "__hash__", "__init__", "__ne__", "__new__", "__reduce__", "__reduce_ex__", "__repr__", "__setattr__", "__str__", "__subclasshook__", "__unicode__", "cell", "class", "columnName", "equals", "fieldAlsoHasFields", "getClass", "getField", "hashCode", "notify", "notifyAll", "project", "toString", "wait" ]

row	value	return dir(cells._obj)
1.	to	[ "__class__", "__copy__", "__deepcopy__", "__delattr__", "__doc__", "__ensure_finalizer__", "__eq__", "__format__", "__getattribute__", "__hash__", "__init__", "__ne__", "__new__", "__reduce__", "__reduce_ex__", "__repr__", "__setattr__", "__str__", "__subclasshook__", "__unicode__", "class", "equals", "fieldAlsoHasFields", "getClass", "getField", "hashCode", "notify", "notifyAll", "project", "row", "toString", "wait" ]

row	value	return dir(row._obj)
1.	to	[ "__class__", "__copy__", "__deepcopy__", "__delattr__", "__doc__", "__ensure_finalizer__", "__eq__", "__format__", "__getattribute__", "__hash__", "__init__", "__ne__", "__new__", "__reduce__", "__reduce_ex__", "__repr__", "__setattr__", "__str__", "__subclasshook__", "__unicode__", "class", "equals", "fieldAlsoHasFields", "getClass", "getField", "hashCode", "notify", "notifyAll", "project", "row", "rowIndex", "toString", "wait" ]

return dir(row._obj.project)
[ "__class__", "__copy__", "__deepcopy__", "__delattr__", "__doc__", "__eq__", "__getattribute__", "__hash__", "__init__", "__ne__", "__new__", "__reduce__", "__reduce_ex__", "__repr__", "__setattr__", "__str__", "__unicode__", "class", "columnModel", "dispose", "equals", "generateID", "getClass", "getLastSave", "getMetadata", "getProcessManager", "hashCode", "history", "id", "lastSave", "loadFromInputStream", "metadata", "notify", "notifyAll", "overlayModels", "processManager", "recordModel", "registerOverlayModel", "rows", "saveToOutputStream", "setLastSave", "toString", "update", "wait" ]
