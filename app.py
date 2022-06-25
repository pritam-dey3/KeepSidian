import dearpygui.dearpygui as dpg


dpg.create_context()
dpg.create_viewport(title='Custom Title', width=700, height=400)

with dpg.font_registry():
    # Download font here: https://fonts.google.com/specimen/Open+Sans
    font = dpg.add_font("OpenSans-Regular.ttf", 15*2, tag="ttf-font")
    dpg.bind_font(font)


with dpg.window(width=700, height=400, ):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
