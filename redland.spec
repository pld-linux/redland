#
# Conditional build:
%bcond_without	mysql		# MySQL support
%bcond_without	pgsql		# PostgreSQL support
%bcond_with	threestore	# 3store support
#
Summary:	Redland - a library that provides a high-level interface for RDF
Summary(pl.UTF-8):	Redland - biblioteka udostępniająca wysokopoziomowy interfejs do RDF
Name:		redland
Version:	1.0.17
Release:	5
License:	LGPL v2.1+ or GPL v2+ or Apache v2.0
Group:		Libraries
Source0:	http://download.librdf.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	e5be03eda13ef68aabab6e42aa67715e
Patch0:		%{name}-LDFLAGS.patch
URL:		http://librdf.org/
%if %{with threestore}
BuildRequires:	3store-devel >= 2.0
BuildRequires:	3store-devel < 3.0
%endif
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	db-devel >= 2
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	libltdl-devel >= 2:2.0
BuildRequires:	libraptor2-devel >= 2.0.7
BuildRequires:	libtool >= 2:2.0
%{?with_mysql:BuildRequires:	mysql-devel >= 3.23.58}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	rasqal-devel >= 1:0.9.25
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	unixODBC-devel
Requires:	libraptor2 >= 2.0.7
Requires:	rasqal >= 1:0.9.25
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Redland is a library that provides a high-level interface for RDF
allowing the RDF graph to be parsed from XML, stored, queried and
manipulated. Redland implements each of the RDF concepts in its own
class via an object based API, reflected into the other language APIs:
Perl, Python, Tcl, Java and Ruby. Some of the classes providing the
parsers, storage mechanisms and other elements are built as modules
that can be added or removed as required.

%description -l pl.UTF-8
Redland to biblioteka udostępniająca wysokopoziomowy interfejs do RDF,
pozwalająca na analizę grafu RDF z XML-a, jego przechowywanie,
odpytywanie i obróbkę. Redland zawiera implementacje każdego pojęcia z
RDF w osobnej klasie poprzez obiekt oparty na API, mający
odzwierciedlenie w API dla innych języków: Perla, Pythona, Tcl-a, Javy
i Ruby'ego. Część klas udostępniających analizatory, mechanizmy
przechowywania i inne elementy jest zbudowana jako moduły, które mogą
być dodawane lub usuwane w razie potrzeby.

%package devel
Summary:	Headers for Redland RDF library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Redland RDF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	db-devel >= 2
Requires:	libltdl-devel >= 2:2.0
Requires:	libraptor2-devel >= 2.0.7
Requires:	rasqal-devel >= 1:0.9.25

%description devel
Headers for Redland RDF library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Redland RDF.

%package static
Summary:	Static Redland RDF library
Summary(pl.UTF-8):	Statyczna biblioteka Redland RDF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Redland RDF library.

%description static -l pl.UTF-8
Statyczna biblioteka Redland RDF.

%package storage-mysql
Summary:	MySQL storage plugin for Redland RDF library
Summary(pl.UTF-8):	Wtyczka przechowywania danych w bazie MySQL dla biblioteki Redland RDF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description storage-mysql
MySQL storage plugin for Redland RDF library.

%description storage-mysql -l pl.UTF-8
Wtyczka przechowywania danych w bazie MySQL dla biblioteki Redland
RDF.

%package storage-postgresql
Summary:	PostgreSQL storage plugin for Redland RDF library
Summary(pl.UTF-8):	Wtyczka przechowywania danych w bazie PostgreSQL dla biblioteki Redland RDF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description storage-postgresql
PostgreSQL storage plugin for Redland RDF library.

%description storage-postgresql -l pl.UTF-8
Wtyczka przechowywania danych w bazie PostgreSQL dla biblioteki
Redland RDF.

%package storage-sqlite
Summary:	SQLite storage plugin for Redland RDF library
Summary(pl.UTF-8):	Wtyczka przechowywania danych w bazie SQLite dla biblioteki Redland RDF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description storage-sqlite
SQLite storage plugin for Redland RDF library.

%description storage-sqlite -l pl.UTF-8
Wtyczka przechowywania danych w bazie SQLite dla biblioteki Redland
RDF.

%package storage-tstore
Summary:	3store storage plugin for Redland RDF library
Summary(pl.UTF-8):	Wtyczka przechowywania danych w bazie 3store dla biblioteki Redland RDF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description storage-tstore
3store storage plugin for Redland RDF library.

%description storage-tstore -l pl.UTF-8
Wtyczka przechowywania danych w bazie 3store dla biblioteki Redland
RDF.

%package storage-virtuoso
Summary:	virtuoso storage plugin for Redland RDF library
Summary(pl.UTF-8):	Wtyczka przechowywania danych w bazie virtuoso dla biblioteki Redland RDF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description storage-virtuoso
virtuoso storage plugin for Redland RDF library.

%description storage-virtuoso -l pl.UTF-8
Wtyczka przechowywania danych w bazie virtuoso dla biblioteki Redland
RDF.

%prep
%setup -q
%patch -P0 -p1

sed -i 's,bdbc_prefix/lib$,bdbc_prefix/%{_lib},' configure.ac

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd libltdl
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd ..
%configure \
	ac_cv_lib_iodbc_SQLConnect=no \
	--disable-ltdl-install \
	--enable-modular \
	--with-html-dir=%{_gtkdocdir} \
        %{!?with_mysql:--with-mysql=no} \
	--with-odbc-inc=/usr/include \
	--with-odbc-lib=/usr/%{_lib} \
        %{!?with_pgsql:--with-postgresql=no} \
	--with-raptor=system \
	--with-rasqal=system \
	--with-threads \
	--with-threestore%{!?with_threestore:=no}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/redland/*.{la,a}
# obsoleted by redland.pc
%{__rm} $RPM_BUILD_ROOT%{_libdir}/librdf.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* FAQS.html LICENSE.html NEWS.html README.html RELEASE.html TODO.html
%attr(755,root,root) %{_bindir}/rdfproc
%attr(755,root,root) %{_bindir}/redland-db-upgrade
%attr(755,root,root) %{_libdir}/librdf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librdf.so.0
%dir %{_libdir}/redland
%dir %{_datadir}/redland
%{?with_mysql:%{_datadir}/redland/mysql-v*.ttl}
%{_mandir}/man1/rdfproc.1*
%{_mandir}/man1/redland-db-upgrade.1*

%files devel
%defattr(644,root,root,755)
%doc docs/{README.html,storage.html}
%attr(755,root,root) %{_bindir}/redland-config
%attr(755,root,root) %{_libdir}/librdf.so
%{_includedir}/librdf.h
%{_includedir}/rdf_*.h
%{_includedir}/redland.h
%{_datadir}/redland/Redland.i
%{_pkgconfigdir}/redland.pc
%{_mandir}/man1/redland-config.1*
%{_mandir}/man3/redland.3*
%{_gtkdocdir}/redland

%files static
%defattr(644,root,root,755)
%{_libdir}/librdf.a

%if %{with mysql}
%files storage-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/redland/librdf_storage_mysql.so
%endif

%if %{with pgsql}
%files storage-postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/redland/librdf_storage_postgresql.so
%endif

%files storage-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/redland/librdf_storage_sqlite.so

%files storage-virtuoso
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/redland/librdf_storage_virtuoso.so

%if %{with threestore}
%files storage-tstore
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/redland/librdf_storage_tstore.so
%endif
