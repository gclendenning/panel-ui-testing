import time

import panel as pn
from app import App

CLICKS = 2

def test_component(page, port):
    # Given
    component = App()
    url = f"http://localhost:{port}"
    # When
    server = pn.serve(component, port=port, threaded=True, show=False)
    time.sleep(0.2)
    # Then
    page.goto(url)
    page.get_by_role("button", name="Run").wait_for()

    for index in range(CLICKS):
        page.get_by_role("button", name="Run").first.click()
        page.get_by_text(f"Finished run {index+1}").wait_for()
    # Clean up
    server.stop()