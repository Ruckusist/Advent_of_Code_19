from int_comp import PainterRobot

app = PainterRobot(manual_input=True)
app.load_program_to_ram(app.test[2])
while True:
    output = app.process(False)
    if type(output) is int:
        print(f"[OUTPUT] {output}")
    if not output: break
