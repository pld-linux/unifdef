Summary:	Unifdef tool for removing ifdef'd lines
Summary(pl.UTF-8):	Narzędzie unifdef do usuwania linii oznaczonych ifdef
Name:		unifdef
Version:	2.10
Release:	1
License:	BSD
Group:		Development/Languages
Source0:	http://dotat.at/prog/unifdef/%{name}-%{version}.tar.xz
# Source0-md5:	bb5d895e5ebbba5c5cc0c2771cf97ebe
URL:		http://dotat.at/prog/unifdef/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unifdef is useful for removing ifdefed lines from a file while
otherwise leaving the file alone. Unifdef acts on '#ifdef', '#ifndef',
'#else', and '#endif' lines, and it knows only enough about C and C++
to know when one of these is inactive because it is inside a comment,
or a single or double quote.

%description -l pl.UTF-8
unifdef jest przydatny do usuwania linii oznaczonych ifdef z pliku
pozostawiając resztę pliku w spokoju. unifdef działa na liniach
'#ifdef', '#ifndef', '#else' i '#endif' i wie o C i C++ tylko tyle,
żeby odróżnić, kiedy któraś z tych dyrektyw jest nieaktywna, ponieważ
jest wewnątrz komentarza lub cudzysłowów.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/unifdef
%attr(755,root,root) %{_bindir}/unifdefall
%{_mandir}/man1/unifdef.1*
%{_mandir}/man1/unifdefall.1*
