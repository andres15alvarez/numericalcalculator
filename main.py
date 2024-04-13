from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import numpy as np
from scipy import optimize

from methods.functions import (
    b1,
    b2,
    df2b,
    df2c,
    f1b,
    f1c,
    f1cc,
    f2b,
    f2c,
    get_f1b_range,
    get_f1c_range,
    get_f2b_range,
    get_f2c_range,
    matrix1,
    matrix2,
)
from methods.roots.bisection import bisection
from methods.roots.newton import newton
from methods.roots.secant import secant
from methods.system_equations.gauss import gauss
from methods.system_equations.gauss_seidel import gauss_seidel
from methods.system_equations.jacobi import jacobi
from utils.image import generate_image


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/roots", response_class=HTMLResponse)
def roots(request: Request):
    return templates.TemplateResponse(request, "roots.html")


@app.get("/equationssystem", response_class=HTMLResponse)
def equationssystem(request: Request):
    return templates.TemplateResponse(request, "equationssystem.html")


@app.get("/roots/1b", response_class=HTMLResponse)
def bisection1b(request: Request):
    results = []
    a, b = get_f1b_range()
    value = bisection(f1b, a, b, results)
    f_value = f1b(value)
    software_value = optimize.bisect(f1b, a, b, xtol=1.0e-5, maxiter=150)
    software_f_value = f1b(software_value)
    generate_image(results, "bisection1b.png")
    image_path = request.url_for("static", path="images/bisection1b.png")
    return templates.TemplateResponse(
        request,
        "roots_solution.html",
        {
            "x": value,
            "fx": f_value,
            "software_x": software_value,
            "software_fx": software_f_value,
            "results": results,
            "image": image_path
        }
    )


@app.get("/roots/1c", response_class=HTMLResponse)
def bisection1c(request: Request):
    results = []
    a, b = get_f1c_range()
    try:
        value = bisection(f1c, a, b, results)
    except Exception as e:
        return templates.TemplateResponse(
            request,
            "roots_solution.html",
            {"message": e}
        )
    f_value = f1c(value)
    software_value = optimize.bisect(f1c, a, b, xtol=1.0e-5, maxiter=150)
    software_f_value = f1c(software_value)
    generate_image(results, "bisection1c.png")
    image_path = request.url_for("static", path="images/bisection1c.png")
    return templates.TemplateResponse(
        request,
        "roots_solution.html",
        {
            "x": value,
            "fx": f_value,
            "software_x": software_value,
            "software_fx": software_f_value,
            "results": results,
            "image": image_path
        }
    )


@app.get("/roots/2b/newton", response_class=HTMLResponse)
def newton2b(request: Request):
    results = []
    value = newton(f2b, df2b, 4, results)
    f_value = f2b(value)
    software_value = optimize.newton(f2b, 4, df2b, tol=1.0e-5, maxiter=150)
    software_f_value = f2b(software_value)
    generate_image(results, "newton2b.png")
    image_path = request.url_for("static", path="images/newton2b.png")
    return templates.TemplateResponse(
        request,
        "roots_solution.html",
        {
            "x": value,
            "fx": f_value,
            "software_x": software_value,
            "software_fx": software_f_value,
            "results": results,
            "image": image_path
        }
    )


@app.get("/roots/2c/newton", response_class=HTMLResponse)
def newton2c(request: Request):
    results = []
    value = newton(f2c, df2c, 1.6, results)
    f_value = f2c(value)
    software_value = optimize.newton(f2c, 1.6, df2c, tol=1.0e-5, maxiter=150)
    software_f_value = f2c(software_value)
    generate_image(results, "newton2c.png")
    image_path = request.url_for("static", path="images/newton2c.png")
    return templates.TemplateResponse(
        request,
        "roots_solution.html",
        {
            "x": value,
            "fx": f_value,
            "software_x": software_value,
            "software_fx": software_f_value,
            "results": results,
            "image": image_path
        }
    )


@app.get("/roots/2b/secant", response_class=HTMLResponse)
def secant2b(request: Request):
    results = []
    a, b = get_f2b_range()
    value = secant(f2b, a, b, results)
    f_value = f2b(value)
    software_value = optimize.root_scalar(
        f2b, method="secant", x0=a, x1=b, xtol=1.0e-5, maxiter=150
    ).root
    software_f_value = f2b(software_value)
    generate_image(results, "secant2b.png")
    image_path = request.url_for("static", path="images/secant2b.png")
    return templates.TemplateResponse(
        request,
        "roots_solution.html",
        {
            "x": value,
            "fx": f_value,
            "software_x": software_value,
            "software_fx": software_f_value,
            "results": results,
            "image": image_path
        }
    )


@app.get("/roots/2c/secant", response_class=HTMLResponse)
def secant2c(request: Request):
    results = []
    a, b = get_f2c_range()
    value = secant(f2c, a, b, results)
    f_value = f2c(value)
    software_value = optimize.root_scalar(
        f2c, method="secant", x0=a, x1=b, xtol=1.0e-5, maxiter=150
    ).root
    software_f_value = f2c(software_value)
    generate_image(results, "secant2c.png")
    image_path = request.url_for("static", path="images/secant2c.png")
    return templates.TemplateResponse(
        request,
        "roots_solution.html",
        {
            "x": value,
            "fx": f_value,
            "software_x": software_value,
            "software_fx": software_f_value,
            "results": results,
            "image": image_path
        }
    )


@app.get("/equationssystem/1", response_class=HTMLResponse)
def equationssystem(request: Request):
    gauss_sol = gauss(matrix1, b1)
    gauss_seidel_sol, gauss_seidel_iter = gauss_seidel(matrix1, b1)
    jacobi_sol, jacobi_iter = jacobi(matrix1, b1)
    software_sol = np.linalg.solve(matrix1, b1)
    return templates.TemplateResponse(
        request,
        "equationssystem_solution.html",
        {
            "gauss_sol": gauss_sol,
            "gauss_seidel_sol": gauss_seidel_sol,
            "jacobi_sol": jacobi_sol,
            "software_sol": software_sol,
            "jacobi_iter": jacobi_iter,
            "gauss_seidel_iter": gauss_seidel_iter
        }
    )

@app.get("/equationssystem/2", response_class=HTMLResponse)
def equationssystem(request: Request):
    gauss_sol = gauss(matrix2, b2)
    gauss_seidel_sol, gauss_seidel_iter = gauss_seidel(matrix2, b2)
    jacobi_sol, jacobi_iter = jacobi(matrix2, b2)
    software_sol = np.linalg.solve(matrix2, b2)
    return templates.TemplateResponse(
        request,
        "equationssystem_solution.html",
        {
            "gauss_sol": gauss_sol,
            "gauss_seidel_sol": gauss_seidel_sol,
            "jacobi_sol": jacobi_sol,
            "software_sol": software_sol,
            "jacobi_iter": jacobi_iter,
            "gauss_seidel_iter": gauss_seidel_iter
        }
    )
