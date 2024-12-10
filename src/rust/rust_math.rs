// rustimport:pyo3

use pyo3::prelude::*;

#[pyfunction]
fn square(n: i32) -> i32 {
    n * n
}
