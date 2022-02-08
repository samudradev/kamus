import pandas as pd

def main():
    """Aku guna skrip ini untuk pindah xlsx ke csv
    """
    data = pd.read_excel(".\data\Daftar Istilah Warna Indonesia--Inggris.xlsx", header=1)
    data = data.drop(labels="Warna", axis=1)
    data.rename(columns={"Bahasa Indonesia ": "Bahasa Indonesia"}, inplace=True)
    data["Inggeris"] = data["Bahasa Inggris "]#.str.replace(", ", ", ")
    data["Alias"] = data["Komentar"].str.extract(r'^Alias (.*)')
    data["Alias"] = data["Alias"].str.strip('"')
    data["Komen"] = data["Komentar"][data["Komentar"].str.contains("Alias") == False]
    data.drop(labels=["Bahasa Inggris ", "Komentar"], axis=1, inplace=True)
    
    data = data.rename(columns={"Inggeris": "Bahasa Inggeris", "Komen": "Komentar"})
    data["Bahasa Inggeris"] = data["Bahasa Inggeris"].str.strip()
    data["Bahasa Indonesia"] = data["Bahasa Indonesia"].str.strip()

    data.to_csv(".\data\Kosa-Kata_Warna_Indonesia_Inggeris.csv", index=False, sep="|")

if __name__ == "__main__":
    main()