import collections
import copy
from .Utils import _write_complex_object

class MessageData(object):
    """Data contract class for type MessageData.
    """
    _defaults = collections.OrderedDict([
        ('ver', 2),
        ('message', None),
        ('severityLevel', None),
        ('properties', {})
    ])
    
    def __init__(self):
        """Initializes a new instance of the class.
        """
        self._values = {
            'ver': 2,
            'message': None,
        }
        self._initialize()
        
    @property
    def ver(self):
        """The ver property.
        
        Returns:
            (int). the property value. (defaults to: 2)
        """
        return self._values['ver']
        
    @ver.setter
    def ver(self, value):
        """The ver property.
        
        Args:
            value (int). the property value.
        """
        self._values['ver'] = value
        
    @property
    def message(self):
        """The message property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        return self._values['message']
        
    @message.setter
    def message(self, value):
        """The message property.
        
        Args:
            value (string). the property value.
        """
        self._values['message'] = value
        
    @property
    def severity_level(self):
        """The severity_level property.
        
        Returns:
            (int). the property value. (defaults to: None)
        """
        if 'severityLevel' in self._values:
            return self._values['severityLevel']
        return self._defaults['severityLevel']
        
    @severity_level.setter
    def severity_level(self, value):
        """The severity_level property.
        
        Args:
            value (int). the property value.
        """
        if value == self._defaults['severityLevel'] and 'severityLevel' in self._values:
            del self._values['severityLevel']
        else:
            self._values['severityLevel'] = value
        
    @property
    def properties(self):
        """The properties property.
        
        Returns:
            (hash). the property value. (defaults to: {})
        """
        if 'properties' in self._values:
            return self._values['properties']
        self._values['properties'] = copy.deepcopy(self._defaults['properties'])
        return self._values['properties']
        
    @properties.setter
    def properties(self, value):
        """The properties property.
        
        Args:
            value (hash). the property value.
        """
        if value == self._defaults['properties'] and 'properties' in self._values:
            del self._values['properties']
        else:
            self._values['properties'] = value
        
    def _initialize(self):
        """Initializes the current instance of the object.
        """
        pass
    
    def write(self):
        """Writes the contents of this object and returns the content as a dict object.
        
        Returns:
            (dict). the object that represents the same data as the current instance.
        """
        return _write_complex_object(self._defaults, self._values)

