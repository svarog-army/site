#!/user/bin/env python
from svarog import create_app
from svarog import commands

app = create_app()
commands.init(app)

if __name__ == "__main__":
    app.run()
