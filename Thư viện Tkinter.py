import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import pandas as pd

TEN_TEP = "danh_sach_nhan_vien.csv"

def luu_csv(du_lieu):
    try:
        with open(TEN_TEP, mode="a", newline="", encoding="utf-8") as tep:
            writer = csv.writer(tep)
            writer.writerow(du_lieu)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu dữ liệu: {e}")

def hien_sinh_nhat_hom_nay():
    try:
        hom_nay = datetime.today().strftime("%d/%m/%Y")
        with open(TEN_TEP, mode="r", encoding="utf-8") as tep:
            reader = csv.reader(tep)
            next(reader)
            ds_sinh_nhat = [dong for dong in reader if dong[4] == hom_nay]
        if ds_sinh_nhat:
            messagebox.showinfo("Sinh nhật hôm nay", "\n".join([f"{dong[1]} ({dong[0]})" for dong in ds_sinh_nhat]))
        else:
            messagebox.showinfo("Sinh nhật hôm nay", "Không có nhân viên nào sinh nhật hôm nay.")
    except FileNotFoundError:
        messagebox.showwarning("Cảnh báo", "Chưa có dữ liệu nhân viên.")

def xuat_excel():
    try:
        du_lieu = pd.read_csv(TEN_TEP)
        du_lieu["Ngày sinh"] = pd.to_datetime(du_lieu["Ngày sinh"], format="%d/%m/%Y")
        du_lieu = du_lieu.sort_values(by="Ngày sinh", ascending=False)
        tep_xuat = "danh_sach_nhan_vien.xlsx"
        du_lieu.to_excel(tep_xuat, index=False)
        messagebox.showinfo("Thành công", f"Dữ liệu đã được xuất ra file {tep_xuat}.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể xuất dữ liệu: {e}")

def them_nhan_vien():
    ma_nv = nhap_ma.get()
    ten_nv = nhap_ten.get()
    don_vi = nhap_don_vi.get()
    chuc_danh = nhap_chuc_danh.get()
    ngay_sinh = nhap_ngay_sinh.get()
    gioi_tinh = gioi_tinh_var.get()
    so_cmnd = nhap_cmnd.get()
    noi_cap = nhap_noi_cap.get()

    if not (ma_nv and ten_nv and don_vi and ngay_sinh and gioi_tinh):
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin.")
        return

    try:
        datetime.strptime(ngay_sinh, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Lỗi", "Ngày sinh không đúng định dạng DD/MM/YYYY.")
        return

    luu_csv([ma_nv, ten_nv, don_vi, chuc_danh, ngay_sinh, gioi_tinh, so_cmnd, noi_cap])
    messagebox.showinfo("Thành công", "Thêm nhân viên thành công!")
    xoa_form()

def xoa_form():
    nhap_ma.delete(0, tk.END)
    nhap_ten.delete(0, tk.END)
    nhap_don_vi.set("")
    nhap_chuc_danh.set("")
    nhap_ngay_sinh.delete(0, tk.END)
    gioi_tinh_var.set("Nam")
    nhap_cmnd.delete(0, tk.END)
    nhap_noi_cap.delete(0, tk.END)

cua_so = tk.Tk()
cua_so.title("Quản lý nhân viên")
khung = ttk.LabelFrame(cua_so, text="Thông tin nhân viên")
khung.grid(column=0, row=0, padx=10, pady=10, sticky="NSEW")

ttk.Label(khung, text="Mã nhân viên:").grid(column=0, row=0, padx=5, pady=5, sticky="E")
nhap_ma = ttk.Entry(khung)
nhap_ma.grid(column=1, row=0, padx=5, pady=5, sticky="W")

ttk.Label(khung, text="Tên nhân viên:").grid(column=0, row=1, padx=5, pady=5, sticky="E")
nhap_ten = ttk.Entry(khung)
nhap_ten.grid(column=1, row=1, padx=5, pady=5, sticky="W")

ttk.Label(khung, text="Đơn vị:").grid(column=0, row=2, padx=5, pady=5, sticky="E")
nhap_don_vi = ttk.Combobox(khung, values=["Phân xướng A", "Phân xướng B", "Phân xướng C"])
nhap_don_vi.grid(column=1, row=2, padx=5, pady=5, sticky="W")

ttk.Label(khung, text="Chức danh:").grid(column=0, row=3, padx=5, pady=5, sticky="E")
nhap_chuc_danh = ttk.Combobox(khung, values=["Nhân viên", "Quản lý", "Giám đốc"])
nhap_chuc_danh.grid(column=1, row=3, padx=5, pady=5, sticky="W")

ttk.Label(khung, text="Ngày sinh (DD/MM/YYYY):").grid(column=0, row=4, padx=5, pady=5, sticky="E")
nhap_ngay_sinh = ttk.Entry(khung)
nhap_ngay_sinh.grid(column=1, row=4, padx=5, pady=5, sticky="W")

ttk.Label(khung, text="Giới tính:").grid(column=0, row=5, padx=5, pady=5, sticky="E")
gioi_tinh_var = tk.StringVar(value="Nam")
ttk.Radiobutton(khung, text="Nam", variable=gioi_tinh_var, value="Nam").grid(column=1, row=5, padx=5, pady=5,
                                                                             sticky="W")
ttk.Radiobutton(khung, text="Nữ", variable=gioi_tinh_var, value="Nữ").grid(column=2, row=5, padx=5, pady=5, sticky="W")

ttk.Label(khung, text="Số CMND:").grid(column=0, row=6, padx=5, pady=5, sticky="E")
nhap_cmnd = ttk.Entry(khung)
nhap_cmnd.grid(column=1, row=6, padx=5, pady=5, sticky="W")

ttk.Label(khung, text="Nơi cấp:").grid(column=0, row=7, padx=5, pady=5, sticky="E")
nhap_noi_cap = ttk.Entry(khung)
nhap_noi_cap.grid(column=1, row=7, padx=5, pady=5, sticky="W")

khung_nut = ttk.Frame(cua_so)
khung_nut.grid(column=0, row=1, padx=10, pady=10, sticky="EW")

ttk.Button(khung_nut, text="Thêm nhân viên", command=them_nhan_vien).grid(column=0, row=0, padx=5, pady=5)
ttk.Button(khung_nut, text="Sinh nhật hôm nay", command=hien_sinh_nhat_hom_nay).grid(column=1, row=0, padx=5, pady=5)
ttk.Button(khung_nut, text="Xuất danh sách", command=xuat_excel).grid(column=2, row=0, padx=5, pady=5)

cua_so.mainloop()