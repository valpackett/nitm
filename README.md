# nitm - Nobody In The Middle

A script that accesses URLs via different Tor circuits, checking the difference.  
Useful for verifying things like PGP keys.

## Usage

```shell
$ nitm -r 10 https://raw.github.com/Whonix/Whonix/master/adrelanos.asc 

Nobody In The Middle using Tor 0.2.4.12-alpha (git-91b8bc26f160f172).

Testing URL https://raw.github.com/Whonix/Whonix/master/adrelanos.asc...
Request 1 of 10:
    requesting new identity...
    doing the HTTP request...
    done!
...
Request 10 of 10:
    requesting new identity...
    doing the HTTP request...
    done!
Yay, https://raw.github.com/Whonix/Whonix/master/adrelanos.asc looks the same via 10 Tor circuits :-)
```

## License

Copyright © 2013 Greg V <floatboth@me.com>  
This work is free. You can redistribute it and/or modify it under the  
terms of the Do What The Fuck You Want To Public License, Version 2,  
as published by Sam Hocevar. See the COPYING file for more details.
