import dearpygui.dearpygui as dpg
from keep2md import convert_all


def callback_fn():
    inp_folder = dpg.get_value("inp_folder")
    print(inp_folder)
    status = convert_all(inp_folder)
    dpg.set_value("output", status)


dpg.create_context()
dpg.create_viewport(title="KeepSidian", width=700, height=400)

with dpg.font_registry():
    # Download font here: https://fonts.google.com/specimen/Open+Sans
    font = dpg.add_font("OpenSans-Regular.ttf", 15 * 2, tag="ttf-font")
    dpg.bind_font(font)


with dpg.window(
    width=700,
    height=400,
):
    dpg.add_text("Put location of folder containing all json files.")
    dpg.add_input_text(default_value="D:\\", tag="inp_folder")
    dpg.add_text("")
    dpg.add_button(label="Convert", callback=callback_fn)
    dpg.add_text("", tag="output")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
