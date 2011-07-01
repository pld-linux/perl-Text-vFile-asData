#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	vFile-asData
Summary:	Text::vFile::asData - parse vFile formatted files into data structures
Summary(pl.UTF-8):	Text::vFile::asData - przetwarzanie plików w formacie vFile na struktury danych
Name:		perl-Text-vFile-asData
Version:	0.07
Release:	1
# "same as perl"
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1f0fc1fbef2111a936db3eb4678ddccc
URL:		http://search.cpan.org/dist/Text-vFile-asData/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Class-Accessor-Chained
%endif
Requires:	perl-Class-Accessor-Chained
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module Text::vFile::asData reads vFile format files, such as
vCard (RFC 2426) and vCalendar (RFC 2445).

%description -l pl.UTF-8
Moduł Perla Text::vFile::asData odczytuje pliki w formacie vFile,
takie jak vCard (RFC 2426) i vCalendar (RFC 2445).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes 
%dir %{perl_vendorlib}/Text/vFile
%{perl_vendorlib}/Text/vFile/asData.pm
%dir %{_examplesdir}/%{name}-%{version}
%dir %{_examplesdir}/%{name}-%{version}/Text-vCard
%{_examplesdir}/%{name}-%{version}/Text-vCard/*
%{_examplesdir}/%{name}-%{version}/Text-vFile
%{_examplesdir}/%{name}-%{version}/rfc2445-objects
%{_mandir}/man3/*
