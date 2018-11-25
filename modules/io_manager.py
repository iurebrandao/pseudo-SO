
class IoManager:
    def __init__(self):
        self.printer_1_used_by = -1
        self.printer_2_used_by = -1
        self.disk_1_used_by = -1
        self.disk_2_used_by = -1
        self.scanner_used_by = -1
        self.modem_used_by = -1

    def getIOdevice(self, process, next_PID):
        # Check if there isn't another process already using the required device
        if process.numero_codigo_da_impresora_requisitada == 1 and self.printer_1_used_by != -1:
            print("IO => A impressora 1 já está sendo utilizada pelo processo " + str(self.printer_1_used_by), end="\n\n")
            return False
        if process.numero_codigo_da_impresora_requisitada == 2 and self.printer_2_used_by != -1:
            print("IO => A impressora 2 já está sendo utilizada pelo processo " + str(self.printer_2_used_by), end="\n\n")
            return False
        if process.numero_codigo_do_disco == 1 and self.disk_1_used_by != -1:
            print("IO => O disco 1 já está sendo utilizado pelo processo " + str(self.disk_1_used_by), end="\n\n")
            return False
        if process.numero_codigo_do_disco == 2 and self.disk_2_used_by != -1:
            print("IO => O disco 2 já está sendo utilizado pelo processo " + str(self.disk_2_used_by), end="\n\n")
            return False
        if process.requisicao_do_scanner == 1 and self.scanner_used_by != -1:
            print("IO => O scanner já está sendo utilizado pelo processo " + str(self.scanner_used_by), end="\n\n")
            return False
        if process.requisicao_do_modem == 1 and self.modem_used_by != -1:
            print("IO => O modem já está sendo utilizado pelo processo " + str(self.modem_used_by), end="\n\n")
            return False

        # Allocates the required device to the process
        if process.numero_codigo_da_impresora_requisitada == 1:
            self.printer_1_used_by = next_PID

        if process.numero_codigo_da_impresora_requisitada == 2:
            self.printer_2_used_by = next_PID

        if process.numero_codigo_do_disco == 1:
            self.disk_1_used_by = next_PID

        if process.numero_codigo_do_disco == 2:
            self.disk_2_used_by = next_PID

        if process.requisicao_do_scanner == 1:
            self.scanner_used_by = next_PID

        if process.requisicao_do_modem == 1:
            self.modem_used_by = next_PID

        return True

    def releaseIOdevice(self, process):
        if self.printer_1_used_by == process.PID:
            self.printer_1_used_by = -1

        if self.printer_2_used_by == process.PID:
            self.printer_2_used_by = -1

        if self.disk_1_used_by == process.PID:
            self.disk_1_used_by = -1

        if self.disk_2_used_by == process.PID:
            self.disk_2_used_by = -1

        if self.scanner_used_by == process.PID:
            self.scanner_used_by = -1

        if self.modem_used_by == process.PID:
            self.modem_used_by = -1
