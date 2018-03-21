from .snakes_cafe import main

try:
    main()
except KeyboardInterrupt:
    print('quit should be used to exit cleanly')
