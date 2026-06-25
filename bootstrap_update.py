from pathlib import Path

files = {
    'index.html': """<!DOCTYPE html>
<html lang=\"es\">

<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Noticias 24/7 - Inicio</title>
    <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-JEO6Qn1B4n6O8G6+4BE1av3S4g1iIrG3O5+b7YG+ixK0pUvpoKnmC5gjbQFH9NuS\" crossorigin=\"anonymous\">
    <link rel=\"stylesheet\" href=\"css/styles.css\">
</head>

<body>
    <div class=\"loader\" id=\"loader\">
        <div class=\"loader__spinner\"></div>
        <div class=\"loader__text\">Cargando...</div>
    </div>

    <nav class=\"navbar navbar-expand-lg navbar-dark bg-dark shadow-sm sticky-top\">
        <div class=\"container\">
            <a class=\"navbar-brand fw-bold\" href=\"index.html\">Noticias 24/7</a>
            <button class=\"navbar-toggler\" type=\"button\" data-bs-toggle=\"collapse\" data-bs-target=\"#mainNavbar\" aria-controls=\"mainNavbar\" aria-expanded=\"false\" aria-label=\"Toggle navigation\">
                <span class=\"navbar-toggler-icon\"></span>
            </button>
            <div class=\"collapse navbar-collapse\" id=\"mainNavbar\">
                <ul class=\"navbar-nav ms-auto mb-2 mb-lg-0\">
                    <li class=\"nav-item\"><a class=\"nav-link active\" aria-current=\"page\" href=\"index.html\">Inicio</a></li>
                    <li class=\"nav-item\"><a class=\"nav-link\" href=\"nosotros.html\">Nosotros</a></li>
                    <li class=\"nav-item\"><a class=\"nav-link\" href=\"servicios.html\">Servicios</a></li>
                    <li class=\"nav-item\"><a class=\"nav-link\" href=\"dashboard.html\">Dashboard</a></li>
                    <li class=\"nav-item\"><a class=\"nav-link\" href=\"contacto.html\">Contacto</a></li>
                </ul>
                <button class=\"btn btn-outline-danger ms-lg-3\" data-bs-toggle=\"modal\" data-bs-target=\"#subscribeModal\">Suscríbete</button>
            </div>
        </div>
    </nav>

    <header class=\"hero text-white d-flex align-items-center\">
        <div class=\"container text-center\">
            <span class=\"badge bg-danger mb-3\">ÚLTIMA HORA</span>
            <h1 class=\"display-5 fw-bold\">Mantente informado con noticias 24/7</h1>
            <p class=\"lead mb-4\">Cobertura profesional, análisis profundo y contenido confiable en un solo lugar.</p>
            <div class=\"d-flex justify-content-center gap-3 flex-wrap\">
                <a href=\"servicios.html\" class=\"btn btn-danger btn-lg\">Ver Servicios</a>
                <button class=\"btn btn-outline-light btn-lg\" data-bs-toggle=\"modal\" data-bs-target=\"#newsModal\">Ver Últimas</button>
            </div>
        </div>
    </header>

    <section class=\"py-5\">
        <div class=\"container\">
            <div class=\"row align-items-center gy-4\">
                <div class=\"col-lg-6\">
                    <h2 class=\"section-title\">Noticias destacadas y análisis profesional</h2>
                    <p class=\"text-muted\">Accede a lo último en política, economía, tecnología y deporte con una plataforma diseñada para presentar la información de forma clara y moderna.</p>
                    <ul class=\"list-unstyled text-muted\">
                        <li class=\"mb-2\">Diseño responsive con Bootstrap.</li>
                        <li class=\"mb-2\">Componentes avanzados: carousel, modal, cards y formularios.</li>
                        <li class=\"mb-2\">Arquitectura CSS limpia y escalable.</li>
                    </ul>
                </div>
                <div class=\"col-lg-6\">
                    <div id=\"homepageCarousel\" class=\"carousel slide shadow-sm rounded-4\" data-bs-ride=\"carousel\">
                        <div class=\"carousel-inner rounded-4 overflow-hidden\">
                            <div class=\"carousel-item active\">
                                <img src=\"img/news-1.jpg\" class=\"d-block w-100\" alt=\"Noticia 1\">
                                <div class=\"carousel-caption d-none d-md-block text-start\">
                                    <h5>Aeropuerto de Chinchero</h5>
                                    <p>Retrasos confirmados en la construcción, análisis y contexto.</p>
                                </div>
                            </div>
                            <div class=\"carousel-item\">
                                <img src=\"img/news-2.jpg\" class=\"d-block w-100\" alt=\"Noticia 2\">
                                <div class=\"carousel-caption d-none d-md-block text-start\">
                                    <h5>Finanzas nacionales</h5>
                                    <p>Apoyo estatal a Petroperú y su impacto en el mercado.</p>
                                </div>
                            </div>
                            <div class=\"carousel-item\">
                                <img src=\"img/news-3.jpg\" class=\"d-block w-100\" alt=\"Noticia 3\">
                                <div class=\"carousel-caption d-none d-md-block text-start\">
                                    <h5>Tecnología en crecimiento</h5>
                                    <p>IA y creatividad transforman sectores clave en el país.</p>
                                </div>
                            </div>
                        </div>
                        <button class=\"carousel-control-prev\" type=\"button\" data-bs-target=\"#homepageCarousel\" data-bs-slide=\"prev\">
                            <span class=\"carousel-control-prev-icon\" aria-hidden=\"true\"></span>
                            <span class=\"visually-hidden\">Anterior</span>
                        </button>
                        <button class=\"carousel-control-next\" type=\"button\" data-bs-target=\"#homepageCarousel\" data-bs-slide=\"next\">
                            <span class=\"carousel-control-next-icon\" aria-hidden=\"true\"></span>
                            <span class=\"visually-hidden\">Siguiente</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class=\"bg-light py-5\">
        <div class=\"container\">
            <div class=\"d-flex justify-content-between align-items-center mb-4 gap-3 flex-column flex-md-row\">
                <div>
                    <h2 class=\"section-title\">Lo que ofrecemos</h2>
                    <p class=\"text-muted mb-0\">Servicios diseñados para medios, marcas y audiencias exigentes.</p>
                </div>
                <button class=\"btn btn-outline-danger\" data-bs-toggle=\"modal\" data-bs-target=\"#servicesModal\">Solicitar asesoría</button>
            </div>
            <div class=\"row row-cols-1 row-cols-md-2 row-cols-xl-3 g-4\">
                <div class=\"col\">
                    <div class=\"card h-100 shadow-sm border-0 rounded-4\">
                        <div class=\"card-body\">
                            <span class=\"badge bg-danger mb-3\">Investigación</span>
                            <h3 class=\"h5\">Reportajes especiales</h3>
                            <p class=\"text-muted\">Contenido de profundidad con análisis, fuentes confiables y visualizaciones claras.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col\">
                    <div class=\"card h-100 shadow-sm border-0 rounded-4\">
                        <div class=\"card-body\">
                            <span class=\"badge bg-danger mb-3\">Cobertura</span>
                            <h3 class=\"h5\">Cobertura 24/7</h3>
                            <p class=\"text-muted\">Seguimos eventos en tiempo real con actualización constante y enfoque periodístico.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col\">
                    <div class=\"card h-100 shadow-sm border-0 rounded-4\">
                        <div class=\"card-body\">
                            <span class=\"badge bg-danger mb-3\">Estrategia</span>
                            <h3 class=\"h5\">Contenido para marcas</h3>
                            <p class=\"text-muted\">Soluciones de comunicación estratégica para clientes que quieren destacar en digital.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class=\"py-5\">
        <div class=\"container\">
            <h2 class=\"section-title text-center mb-5\">Noticias destacadas</h2>
            <div class=\"row row-cols-1 row-cols-md-2 row-cols-xl-3 g-4\">
                <div class=\"col\">
                    <div class=\"card news-card h-100 border-0 shadow-sm rounded-4 overflow-hidden\">
                        <img src=\"img/news-4.jpg\" class=\"card-img-top\" alt=\"Deportes\">
                        <div class=\"card-body\">
                            <span class=\"badge bg-danger mb-2\">Deportes</span>
                            <h3 class=\"h5\">Mundial 2026: la mayor cita del fútbol</h3>
                            <p class=\"text-muted\">Sigue el avance de los equipos, fechas y estadísticas más relevantes del torneo.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col\">
                    <div class=\"card news-card h-100 border-0 shadow-sm rounded-4 overflow-hidden\">
                        <img src=\"img/news-5.jpg\" class=\"card-img-top\" alt=\"Ciencia\">
                        <div class=\"card-body\">
                            <span class=\"badge bg-danger mb-2\">Ciencia</span>
                            <h3 class=\"h5\">James Webb revela exoplaneta</h3>
                            <p class=\"text-muted\">La primera imagen directa de una superficie extraterrestre renueva el interés científico global.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col\">
                    <div class=\"card news-card h-100 border-0 shadow-sm rounded-4 overflow-hidden\">
                        <img src=\"img/news-3.jpg\" class=\"card-img-top\" alt=\"Tecnología\">
                        <div class=\"card-body\">
                            <span class=\"badge bg-danger mb-2\">Tecnología</span>
                            <h3 class=\"h5\">IA al servicio de la toma de decisiones</h3>
                            <p class=\"text-muted\">Cómo los sistemas inteligentes están cambiando la comunicación y la investigación.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class=\"footer bg-dark text-white py-5\">
        <div class=\"container\">
            <div class=\"row gy-4\">
                <div class=\"col-md-4\">
                    <h5>Noticias 24/7</h5>
                    <p class=\"text-muted\">Plataforma profesional de noticias con enfoque en periodismo riguroso y diseño web moderno.</p>
                </div>
                <div class=\"col-md-4\">
                    <h5>Contacto</h5>
                    <p class=\"text-muted mb-1\">contacto@noticias247.com</p>
                    <p class=\"text-muted\">+51 956 234 567</p>
                </div>
                <div class=\"col-md-4\">
                    <h5>Redes</h5>
                    <div class=\"d-flex gap-2 flex-wrap\">
                        <a class=\"btn btn-outline-light btn-sm\" href=\"#\">Facebook</a>
                        <a class=\"btn btn-outline-light btn-sm\" href=\"#\">Twitter</a>
                        <a class=\"btn btn-outline-light btn-sm\" href=\"#\">Instagram</a>
                    </div>
                </div>
            </div>
            <div class=\"text-center text-muted mt-4\">&copy; 2026 Noticias 24/7. Todos los derechos reservados.</div>
        </div>
    </footer>

    <div class=\"modal fade\" id=\"newsModal\" tabindex=\"-1\" aria-labelledby=\"newsModalLabel\" aria-hidden=\"true\">
        <div class=\"modal-dialog modal-dialog-centered modal-lg\">
            <div class=\"modal-content border-0 rounded-4 shadow-lg\">
                <div class=\"modal-header border-0\">
                    <h5 class=\"modal-title\" id=\"newsModalLabel\">Últimas noticias destacadas</h5>
                    <button type=\"button\" class=\"btn-close\" data-bs-dismiss=\"modal\" aria-label=\"Cerrar\"></button>
                </div>
                <div class=\"modal-body\">
                    <p>Revisa los temas más relevantes del día y descubre el análisis completo de nuestras coberturas principales.</p>
                    <ul>
                        <li>Aeropuerto de Chinchero: riesgos y oportunidades para la economía regional.</li>
                        <li>Petroperú recibe soporte financiero: ¿qué implica para el mercado?</li>
                        <li>La IA en la era post-pandemia: efectos en tecnología y educación.</li>
                    </ul>
                </div>
                <div class=\"modal-footer border-0\">
                    <button type=\"button\" class=\"btn btn-secondary\" data-bs-dismiss=\"modal\">Cerrar</button>
                    <a href=\"nosotros.html\" class=\"btn btn-danger\">Conoce nuestro equipo</a>
                </div>
            </div>
        </div>
    </div>

    <div class=\"modal fade\" id=\"servicesModal\" tabindex=\"-1\" aria-labelledby=\"servicesModalLabel\" aria-hidden=\"true\">
        <div class=\"modal-dialog modal-dialog-centered\">
            <div class=\"modal-content border-0 rounded-4 shadow-lg\">
                <div class=\"modal-header border-0\">
                    <h5 class=\"modal-title\" id=\"servicesModalLabel\">Solicita asesoría</h5>
                    <button type=\"button\" class=\"btn-close\" data-bs-dismiss=\"modal\" aria-label=\"Cerrar\"></button>
                </div>
                <div class=\"modal-body\">
                    <p>Contáctanos para recibir una propuesta personalizada en comunicación, contenidos y cobertura digital.</p>
                    <div class=\"d-grid gap-2\">
                        <a href=\"contacto.html\" class=\"btn btn-danger\">Ir a contacto</a>
                        <button class=\"btn btn-outline-secondary\" type=\"button\" data-bs-dismiss=\"modal\">Cerrar</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class=\"modal fade\" id=\"subscribeModal\" tabindex=\"-1\" aria-labelledby=\"subscribeModalLabel\" aria-hidden=\"true\">
        <div class=\"modal-dialog modal-dialog-centered\">
            <div class=\"modal-content border-0 rounded-4 shadow-lg\">
                <div class=\"modal-header border-0\">
                    <h5 class=\"modal-title\" id=\"subscribeModalLabel\">Suscripción</h5>
                    <button type=\"button\" class=\"btn-close\" data-bs-dismiss=\"modal\" aria-label=\"Cerrar\"></button>
                </div>
                <div class=\"modal-body\">
                    <p>Regístrate para recibir alertas y boletines semanales directamente en tu correo.</p>
                    <form>
                        <div class=\"mb-3\">
                            <label for=\"subscribeEmail\" class=\"form-label\">Correo electrónico</label>
                            <input type=\"email\" class=\"form-control\" id=\"subscribeEmail\" placeholder=\"tunombre@correo.com\">
                        </div>
                        <button type=\"button\" class=\"btn btn-danger w-100\">Enviar</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-gm2Mw0DxI1kW9Px+DbtKm3qY5xNrbL1jGd7ifpGIfkdYyPv64eG2X1qRhxop6H2M\" crossorigin=\"anonymous\"></script>
    <script src=\"js/menu.js\"></script>
</body>
</html>""",
    'nosotros.html': """<!DOCTYPE html>
<html lang=\"es\">

<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Noticias 24/7 - Nosotros</title>
    <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-JEO6Qn1B4n6O8G6+4BE1av3S4g1iIrG3O5+b7YG+ixK0pUvpoKnmC5gjbQFH9NuS\" crossorigin=\"anonymous\">
    <link rel=\"stylesheet\" href=\"css/styles.css\">
</head>

<body>
    <div class=\"loader\" id=\"loader\">
        <div class=\"loader__spinner\"></div>
        <div class=\"loader__text\">Cargando...</div>
    </div>

    <nav class=\"navbar navbar-expand-lg navbar-dark bg-dark shadow-sm sticky-top\">
        <div class=\"container\">
            <a class=\"navbar-brand fw-bold\" href=\"index.html\">Noticias 24/7</a>
            <button class=\"navbar-toggler\" type=\"button\" data-bs-toggle=\"collapse\" data-bs-target=\"#mainNavbar\" aria-controls=\"mainNavbar\" aria-expanded=\"false\" aria-label=\"Toggle navigation\">
                <span class=\"navbar-toggler-icon\"></span>
            </button>
            <div class=\"collapse navbar-collapse\" id=\"mainNavbar\">
                <ul class=\"navbar-nav ms-auto mb-2 mb-lg-0\">
                    <li class=\"nav-item\"><a class=\"nav-link\" href=\"index.html\">Inicio</a></li>
                    <li class=\"nav-item\"><a class=\"nav-link active\" aria-current=\"page\" href=\"nosotros.html\">Nosotros</a></li>
                    <li class=\"nav-item\"><a class=\"nav-link\" href=\"servicios.html\">Servicios</a></li>
                    <li class=\"nav-item\"><a class=\"nav-link\" href=\"dashboard.html\">Dashboard</a></li>
                    <li class=\"nav-item\"><a class=\"nav-link\" href=\"contacto.html\">Contacto</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <section class=\"page-hero page-hero-dark text-white py-5\">
        <div class=\"container text-center\">
            <h1 class=\"display-5 fw-bold\">Nuestra misión es informar con propósito</h1>
            <p class=\"lead text-white-75\">Combinamos periodismo responsable con un diseño web profesional para llegar a tu audiencia.</p>
        </div>
    </section>

    <section class=\"py-5\">
        <div class=\"container\">
            <div class=\"row gy-4 align-items-center\">
                <div class=\"col-lg-6\">
                    <h2 class=\"section-title\">Sobre Nosotros</h2>
                    <p class=\"text-muted\">Noticias 24/7 nace como un medio digital orientado a entregar contenido riguroso y oportuno. Nuestra arquitectura de trabajo incluye investigación, verificación y formatos dinámicos para cada plataforma.</p>
                    <p class=\"text-muted\">Con un equipo de profesionales en periodismo, diseño y tecnología, desarrollamos piezas que ayudan a los lectores a entender el contexto detrás de cada noticia.</p>
                    <button class=\"btn btn-danger btn-lg\" data-bs-toggle=\"modal\" data-bs-target=\"#teamModal\">Conoce al equipo</button>
                </div>
                <div class=\"col-lg-6\">
                    <div class=\"ratio ratio-16x9 rounded-4 overflow-hidden shadow-sm\">
                        <img src=\"img/redaccion.jpg\" alt=\"Equipo de redacción\" class=\"w-100 h-100 object-fit-cover\">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class=\"bg-light py-5\">
        <div class=\"container\">
            <div class=\"row row-cols-1 row-cols-md-3 g-4\">
                <div class=\"col\">
                    <div class=\"card border-0 shadow-sm h-100 rounded-4\">
                        <div class=\"card-body\">
                            <h3 class=\"h5\">Valores</h3>
                            <p class=\"text-muted\">Transparencia, veracidad y compromiso con el lector son el núcleo de nuestra editorial.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col\">
                    <div class=\"card border-0 shadow-sm h-100 rounded-4\">
                        <div class=\"card-body\">
                            <h3 class=\"h5\">Metodología</h3>
                            <p class=\"text-muted\">Cada publicación pasa por verificación de datos y revisión editorial para asegurar calidad.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col\">
                    <div class=\"card border-0 shadow-sm h-100 rounded-4\">
                        <div class=\"card-body\">
                            <h3 class=\"h5\">Visión</h3>
                            <p class=\"text-muted\">Convertirnos en la plataforma líder de noticias digitales en América Latina con un diseño moderno y accesible.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class=\"py-5\">
        <div class=\"container\">
            <h2 class=\"section-title text-center mb-5\">Equipo</h2>
            <div class=\"row row-cols-1 row-cols-md-3 g-4\">
                <div class=\"col\">
                    <div class=\"card border-0 shadow-sm h-100 text-center p-4 rounded-4\">
                        <img src=\"img/team-1.jpg\" class=\"rounded-circle mx-auto d-block mb-3\" alt=\"Ana Martínez\" width=\"150\" height=\"150\">
                        <div class=\"card-body\">
                            <h3 class=\"h5\">Ana Martínez</h3>
                            <p class=\"text-muted\">Directora Editorial</p>
                            <button class=\"btn btn-sm btn-danger\" data-bs-toggle=\"modal\" data-bs-target=\"#teamModal\">Ver perfil</button>
                        </div>
                    </div>
                </div>
                <div class=\"col\">
                    <div class=\"card border-0 shadow-sm h-100 text-center p-4 rounded-4\">
                        <img src=\"img/team-2.jpg\" class=\"rounded-circle mx-auto d-block mb-3\" alt=\"Carlos Rodríguez\" width=\"150\" height=\"150\">
                        <div class=\"card-body\">
                            <h3 class=\"h5\">Carlos Rodríguez</h3>
                            <p class=\"text-muted\">Editor en Jefe</p>
                            <button class=\"btn btn-sm btn-danger\" data-bs-toggle=\"modal\" data-bs-target=\"#teamModal\">Ver perfil</button>
                        </div>
                    </div>
                </div>
                <div class=\"col\">
                    <div class=\"card border-0 shadow-sm h-100 text-center p-4 rounded-4\">
                        <img src=\"img/team-3.jpg\" class=\"rounded-circle mx-auto d-block mb-3\" alt=\"María González\" width=\"150\" height=\"150\">
                        <div class=\"card-body\">
                            <h3 class=\"h5\">María González</h3>
                            <p class=\"text-muted\">Reportera Internacional</p>
                            <button class=\"btn btn-sm btn-danger\" data-bs-toggle=\"modal\" data-bs-target=\"#teamModal\">Ver perfil</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class=\"footer bg-dark text-white py-5\">
        <div class=\"container\">
            <div class=\"row gy-4\">
                <div class=\"col-md-4\">
                    <h5>Noticias 24/7</h5>
                    <p class=\"text-muted\">Equipo dedicado a crear noticias con la mejor presentación y criterios periodísticos.</p>
                </div>
                <div class=\"col-md-4\">
                    <h5>Ubicación</h5>
                    <p class=\"text-muted mb-1\">Av. Grau 245, Ica, Perú</p>
                </div>
                <div class=\"col-md-4\">
                    <h5>Síguenos</h5>
                    <div class=\"d-flex gap-2 flex-wrap\">
                        <a class=\"btn btn-outline-light btn-sm\" href=\"#\">Facebook</a>
                        <a class=\"btn btn-outline-light btn-sm\" href=\"#\">Twitter</a>
                    </div>
                </div>
            </div>
            <div class=\"text-center text-muted mt-4\">&copy; 2026 Noticias 24/7. Todos los derechos reservados.</div>
        </div>
    </footer>

    <div class=\"modal fade\" id=\"teamModal\" tabindex=\"-1\" aria-labelledby=\"teamModalLabel\" aria-hidden=\"true\">
        <div class=\"modal-dialog modal-dialog-centered\">
            <div class=\"modal-content border-0 rounded-4 shadow-lg\">
                <div class=\"modal-header border-0\">
                    <h5 class=\"modal-title\" id=\"teamModalLabel\">Equipo editorial</h5>
                    <button type=\"button\" class=\"btn-close\" data-bs-dismiss=\"modal\" aria-label=\"Cerrar\"></button>
                </div>
                <div class=\"modal-body\">
                    <p>Nuestro equipo combina experiencia en periodismo digital, diseño editorial y análisis informativo para entregar contenido de calidad.</p>
                    <ul class=\"list-unstyled text-muted\">
                        <li><strong>Ana Martínez</strong> - dirige las operaciones editoriales y supervisa la calidad.</li>
                        <li><strong>Carlos Rodríguez</strong> - coordina las coberturas y garantiza fuentes confiables.</li>
                        <li><strong>María González</strong> - reporta desde escenarios internacionales con enfoque humano.</li>
                    </ul>
                </div>
                <div class=\"modal-footer border-0\">
                    <button type=\"button\" class=\"btn btn-secondary\" data-bs-dismiss=\"modal\">Cerrar</button>
                </div>
            </div>
        </div>
    </div>

    <script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-gm2Mw0DxI1kW9Px+DbtKm3qY5xNrbL1jGd7ifpGIfkdYyPv64eG2X1qRhxop6H2M\" crossorigin=\"anonymous\"></script>
    <script src=\"js/menu.js\"></script>
</body>
</html>""",
    'servicios.html': """<!DOCTYPE html>
<html lang=\"es\">

<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Noticias 24/7 - Servicios</title>
    <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-JEO6Qn1B4n6O8G6+4BE1av3S4g1iIrG3O5+b7YG+ixK0pUvpoKnmC5gjbQFH9NuS\" crossorigin=\"anonymous\">
    <link rel=\"stylesheet\" href=\"css/styles.css\">
</head>

<body>
    <div class=\"loader\" id=\"loader\">
        <div class=\"loader__spinner\"></div>
        <div class=\"loader__text\">Cargando...</div>
    </div>

    <nav class=\"navbar navbar-expand-lg navbar-dark bg-dark shadow-sm sticky-top\">
        <div class=\"container\">
            <a class=\"navbar-brand fw-bold\" href=\"index.html\">Noticias 24/7</a>
            <button class=\"navbar-toggler\" type=\"button\" data-bs-toggle=\"collapse\" data-bs-target=\"#mainNavbar\" aria-controls=\"mainNavbar\" aria-expanded=\"false\" aria-label=\"Toggle navigation\">
                <span class=\"navbar-toggler-icon\"></span>
            </button>
            <div class=\"collapse navbar-collapse\" id=\"mainNavbar\">
                <ul class=\"navbar-nav ms-auto mb-2 mb-lg-0\">
                    <li class=\"nav-item\"><a class=\"nav-link\" href=\"index.html\">Inicio</a></li>
                    <li class=\"nav-item\"><a class=\"nav-link\" href=\"nosotros.html\">Nosotros</a></li>
                    <li class=\"nav-item\"><a class=\"nav-link active\" aria-current=\"page\" href=\"servicios.html\">Servicios</a></li>
                    <li class=\"nav-item\"><a class=\"nav-link\" href=\"dashboard.html\">Dashboard</a></li>
                    <li class=\"nav-item\"><a class=\"nav-link\" href=\"contacto.html\">Contacto</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <section class=\"page-hero page-hero-dark text-white py-5\">
        <div class=\"container text-center\">
            <h1 class=\"display-5 fw-bold\">Servicios de comunicación y análisis digital</h1>
            <p class=\"lead text-white-75\">Soluciones integradas para medios, marcas e instituciones que requieren una voz profesional y moderna.</p>
        </div>
    </section>

    <section class=\"py-5\">
        <div class=\"container\">
            <div class=\"row g-4\">
                <div class=\"col-md-6 col-xl-4\">
                    <div class=\"card border-0 shadow-sm h-100 rounded-4\">
                        <div class=\"card-body\">
                            <span class=\"badge bg-danger mb-3\">Estrategia</span>
                            <h3 class=\"h5\">Consultoría editorial</h3>
                            <p class=\"text-muted\">Armamos planes de contenido, editorial y pauta para impulsar tu alcance digital.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col-md-6 col-xl-4\">
                    <div class=\"card border-0 shadow-sm h-100 rounded-4\">
                        <div class=\"card-body\">
                            <span class=\"badge bg-danger mb-3\">Producción</span>
                            <h3 class=\"h5\">Cobertura en vivo</h3>
                            <p class=\"text-muted\">Transmisiones e informes desde terreno con comunicación profesional y confiable.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col-md-6 col-xl-4\">
                    <div class=\"card border-0 shadow-sm h-100 rounded-4\">
                        <div class=\"card-body\">
                            <span class=\"badge bg-danger mb-3\">Contenido</span>
                            <h3 class=\"h5\">Editorial digital</h3>
                            <p class=\"text-muted\">Artículos, reportajes y piezas multimedia diseñadas para usuarios exigentes.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col-md-6 col-xl-4\">
                    <div class=\"card border-0 shadow-sm h-100 rounded-4\">
                        <div class=\"card-body\">
                            <span class=\"badge bg-danger mb-3\">Optimización</span>
                            <h3 class=\"h5\">Redes sociales</h3>
                            <p class=\"text-muted\">Comunicación estratégica con formatos adaptados para redes y campañas de alto impacto.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col-md-6 col-xl-4\">
                    <div class=\"card border-0 shadow-sm h-100 rounded-4\">
                        <div class=\"card-body\">
                            <span class=\"badge bg-danger mb-3\">Auditoría</span>
                            <h3 class=\"h5\">Análisis de medios</h3>
                            <p class=\"text-muted\">Reportes de audiencia y desempeño para mejorar la toma de decisiones.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col-md-6 col-xl-4\">
                    <div class=\"card border-0 shadow-sm h-100 rounded-4\">
                        <div class=\"card-body\">
                            <span class=\"badge bg-danger mb-3\">Soporte</span>
                            <h3 class=\"h5\">Comunicación corporativa</h3>
                            <p class=\"text-muted\">Apoyamos la difusión institucional con mensajes claros, confiables y alineados a objetivos.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class=\"bg-light py-5\">
        <div class=\"container\">
            <div class=\"row align-items-center gy-4\">
                <div class=\"col-lg-6\">
                    <h2 class=\"section-title\">Planes adaptados</h2>
                    <p class=\"text-muted\">Elige el plan ideal según tus necesidades y escala con soluciones integrales.</p>
                </div>
                <div class=\"col-lg-6 text-lg-end\">
                    <button class=\"btn btn-danger btn-lg\" data-bs-toggle=\"modal\" data-bs-target=\"#quoteModal\">Solicitar cotización</button>
                </div>
            </div>
            <div class=\"row row-cols-1 row-cols-md-3 g-4 mt-4\">
                <div class=\"col\">
                    <div class=\"card border-0 shadow-sm h-100 rounded-4\">
                        <div class=\"card-body\">
                            <h3 class=\"h5\">Básico</h3>
                            <p class=\"text-muted\">Cobertura de noticias y soporte editorial para pequeñas campañas.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col\">
                    <div class=\"card border-0 shadow-sm h-100 rounded-4\">
                        <div class=\"card-body\">
                            <h3 class=\"h5\">Avanzado</h3>
                            <p class=\"text-muted\">Proyectos de contenido continuo, análisis y publicaciones estables.</p>
                        </div>
                    </div>
                </div>
                <div class=\"col\">
                    <div class=\"card border-0 shadow-sm h-100 rounded-4\">
                        <div class=\"card-body\">
                            <h3 class=\"h5\">Premium</h3>
                            <p class=\"text-muted\">Cobertura 24/7, informes especiales y estrategia integral de comunicación.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class=\"footer bg-dark text-white py-5\">
        <div class=\"container\">
            <div class=\"row gy-4\">
                <div class=\"col-md-4\">
                    <h5>Noticias 24/7</h5>
                    <p class=\"text-muted\">Servicios escalables con un diseño web profesional.</p>
                </div>
                <div class=\"col-md-4\">
                    <h5>Soporte</h5>
                    <p class=\"text-muted mb-1\">contacto@noticias247.com</p>
                    <p class=\"text-muted\">+51 956 234 567</p>
                </div>
                <div class=\"col-md-4\">
                    <h5>Acceso</h5>
                    <a href=\"dashboard.html\" class=\"btn btn-outline-light btn-sm\">Dashboard</a>
                </div>
            </div>
            <div class=\"text-center text-muted mt-4\">&copy; 2026 Noticias 24/7. Todos los derechos reservados.</div>
        </div>
    </footer>

    <div class=\"modal fade\" id=\"quoteModal\" tabindex=\"-1\" aria-labelledby=\"quoteModalLabel\" aria-hidden=\"true\">
        <div class=\"modal-dialog modal-dialog-centered\">
            <div class=\"modal-content border-0 rounded-4 shadow-lg\">
                <div class=\"modal-header border-0\">
                    <h5 class=\"modal-title\" id=\"quoteModalLabel\">Cotización personalizada</h5>
                    <button type=\"button\" class=\"btn-close\" data-bs-dismiss=\"modal\" aria-label=\"Cerrar\"></button>
                </div>
                <div class=\"modal-body\">
                    <p>Cuéntanos tu proyecto y te ayudamos a definir el mejor plan de comunicación.</p>
                    <a href=\"contacto.html\" class=\"btn btn-danger w-100\">Contactar ahora</a>
                </div>
            </div>
        </div>
    </div>

    <script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-gm2Mw0DxI1kW9Px+DbtKm3qY5xNrbL1jGd7ifpGIfkdYyPv64eG2X1qRhxop6H2M\" crossorigin=\"anonymous\"></script>
    <script src=\"js/menu.js\"></script>
</body>
</html>""",
}

for path, content in files.items():
    Path(path).write_text(content, encoding='utf-8')

print('Bootstrap site files updated.')
"}
Path('c:/Users/USUARIO/PC2/bootstrap_update.py').write_text(script, encoding='utf-8')
