%include	/usr/lib/rpm/macros.perl
Summary:	Net-ICQ perl module
Summary(pl):	Modu³ perla Net-ICQ
Name:		perl-Net-ICQ
Version:	0.08
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-ICQ-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Text-LineEditor
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-Text-LineEditor
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Net-ICQ - simple ICQ client in Perl. 

%description -l pl
Net-ICQ - prosty klient ICQ.

%prep
%setup -q -n Net-ICQ-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/ICQ
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README* TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README*,TODO}.gz client.pl

%{perl_sitelib}/Net/ICQ.pm
%{perl_sitearch}/auto/Net/ICQ

%{_mandir}/man3/*
