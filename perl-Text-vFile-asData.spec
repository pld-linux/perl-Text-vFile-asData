#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	vFile-asData
Summary:	perl(Text::vFile::asData)
Name:		perl-Text-vFile-asData
Version:	0.05
Release:	0.1
# "same as perl"
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3e2ec1f22562dc3d92ababac4f882bed
URL:		http://search.cpan.org/dist/Text-vFile-asData
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Class-Accessor-Chained
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module Text::vFile::asData reads vFile format files, such as vCard (RFC 2426) and vCalendar (RFC 2445).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
# if module isn't noarch, use:
# %{__make} \
#	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes 
# Text-vCard  Text-vFile*
# note it's mostly easier to copy unpackaged filelist here, and run adapter over the spec.
# use macros:
%{perl_vendorlib}/Text/vFile/asData.pm
%dir %attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%dir %attr(755,root,root) %{_examplesdir}/%{name}-%{version}/Text-vCard
%{_examplesdir}/%{name}-%{version}/Text-vCard/*
%dir %attr(755,root,root) %{_examplesdir}/%{name}-%{version}/Text-vFile
%{_examplesdir}/%{name}-%{version}/Text-vFile
%dir %attr(755,root,root) %{_examplesdir}/%{name}-%{version}/rfc2445-objects
%{_examplesdir}/%{name}-%{version}/rfc2445-objects
%{_mandir}/man3/*
