import os
import time
import docx
import openpyxl
from selenium.webdriver.common.by import By
from docx import Document
from docx.shared import Inches
from selenium.webdriver import Keys, ActionChains

from Utilities.Config import screenshot_folder, root_dir


class Functions:

    def bookmark(self, module, ts_id, tc_id, step_num):
        path = screenshot_folder + f'{module}\\{ts_id}'
        document = Document(path + f'\\{ts_id}.docx')
        table = document.add_table(rows=0, cols=1, style=document.styles['Table Grid'])

        if step_num == 'Step 1':
            data_row = table.add_row().cells
            data_row[0].text = self.get_tc_name(module, tc_id)  # Get_TC_bookmark

        if len(self.get_tc(module, tc_id, step_num)[0]) > 0:
            if step_num != 'Step 1':
                document.add_page_break()

            data_row = table.add_row().cells
            data_row[0].text = step_num + " - " + self.get_tc(module, tc_id, step_num)[0]  # Get_Step_bookmark
            data_row = table.add_row().cells
            data_row[0].text = self.get_tc(module, tc_id, step_num)[1]

        document.save(path + f'\\{ts_id}.docx')  # update document

    def screen_capture(self, driver, module, ts_id, tc_id, step_num):
        time.sleep(2)
        path = screenshot_folder + f'{module}\\{ts_id}'
        document = Document(path + f'\\{ts_id}.docx')
        driver.save_screenshot(path + f'/{ts_id}_{tc_id} {step_num}.png')
        p = document.add_paragraph()
        r = p.add_run()
        r.add_picture(path + f'/{ts_id}_{tc_id} {step_num}.png', width=Inches(5.8))

        document.save(path + f'\\{ts_id}.docx')  # update document

    def tag_status(self, module, ts_id, status):
        path = screenshot_folder + f'{module}\\{ts_id}'
        document = Document(path + f'\\{ts_id}.docx')
        document.add_page_break()
        document.add_paragraph(status)
        document.save(path + f'\\{ts_id}.docx')

    def create_document(self, driver, module, ts_id):
        path = screenshot_folder + f'{module}\\{ts_id}'
        document = docx.Document()

        is_exist = os.path.exists(path)
        if not is_exist:
            os.mkdir(path)

        table = document.add_table(rows=1, cols=1, style=document.styles['Table Grid'])
        row = table.rows[0].cells
        row[0].text = ts_id + " - " + self.get_ts(module, ts_id)
        document.add_paragraph()
        document.save(path + f'\\{ts_id}.docx')

    def get_ts(self, module, ts_id):
        workbook = openpyxl.load_workbook(root_dir.parent/f'Config/{module}.xlsx')
        sheet = workbook["AT - Test Suite"]
        total_rows = sheet.max_row
        data = ""
        for i in range(2, total_rows + 1):
            if sheet.cell(row=i, column=1).value == ts_id:
                data = sheet.cell(row=i, column=2).value
        return data

    def get_tc(self, module, tc_id, step_num):
        workbook = openpyxl.load_workbook(root_dir.parent/f'Config/{module}.xlsx')
        sheet = workbook["AT - Test Case"]
        total_rows = sheet.max_row
        description = ""
        expected = ""

        for i in range(2, total_rows + 1):
            if sheet.cell(row=i, column=1).value == tc_id and sheet.cell(row=i, column=2).value == step_num:
                description = sheet.cell(row=i, column=3).value
                expected = sheet.cell(row=i, column=4).value

        return description, expected

    def get_tc_name(self, module, tc_id):
        workbook = openpyxl.load_workbook(root_dir.parent/f'Config/{module}.xlsx')
        sheet = workbook["AT - Test Case"]
        total_rows = sheet.max_row
        tc_name = ""

        for i in range(2, total_rows + 1):
            if tc_id + "_" in sheet.cell(row=i, column=1).value:
                tc_name = sheet.cell(row=i, column=1).value

        return tc_name

    def new_tab(self, driver, url):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(url)
        curr = driver.current_window_handle
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if handle != curr:
                driver.close()
