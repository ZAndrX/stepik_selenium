import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_btn_add_to_basket(browser_op):
    browser_op.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert browser_op.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
