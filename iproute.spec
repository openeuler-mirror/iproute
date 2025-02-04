Name:		iproute
Version:	5.18.0
Release:	1
Summary:	Linux network configuration utilities
License:	GPLv2+ and Public Domain
URL:		https://kernel.org/pub/linux/utils/net/iproute2/
Source0:	https://mirrors.edge.kernel.org/pub/linux/utils/net/iproute2/iproute2-%{version}.tar.xz

Patch1:         bugfix-iproute2-3.10.0-fix-maddr-show.patch         
Patch2:         bugfix-iproute2-change-proc-to-ipnetnsproc-which-is-private.patch

BuildRequires:	gcc bison elfutils-libelf-devel flex iptables-devel
BuildRequires:  libmnl-devel libselinux-devel pkgconfig libbpf-devel
Requires:       libbpf psmisc

Provides:       /sbin/ip iproute-tc tc 
Obsoletes:      iproute-tc 

%description
Iproute2 is a collection of user-space utilities to set up networking
under Linux from the command-line. It can inspect and configure,
among other things: interface paramters, IP addresses, routing,
tunnels, bridges, packet transformations (IPsec, etc.), and Quality
of Service.

%package        devel
Summary:        Header files for iprout2
License:        GPLv2+
Provides:       iproute-static = %{version}-%{release}
Obsoletes:      iproute-static < %{version}-%{release}

%description    devel
Header files for iprout2

%package_help

%prep
%autosetup -n %{name}2-%{version} -p1

%build
export LIBDIR='%{_libdir}'
export IPT_LIB_DIR='/%{_lib}/xtables'
%configure
%make_build

%install
export CONFDIR='%{_sysconfdir}/iproute2'
export SBINDIR='%{_sbindir}'
export LIBDIR='%{_libdir}'
export DOCDIR='%{_docdir}'

%make_install 

install -m 0755 -d %{buildroot}%{_includedir}
install -m 0644 include/libnetlink.h %{buildroot}%{_includedir}/libnetlink.h
install -m 0644 lib/libnetlink.a %{buildroot}%{_libdir}/libnetlink.a

%files
%defattr(-,root,root)
%license COPYING
%doc README
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/iproute2/*
%{_sbindir}/*
%{_libdir}/tc/*
%{_datadir}/bash-completion/completions/*

%files         devel
%defattr(-,root,root)
%license COPYING
%{_libdir}/libnetlink.a
%{_includedir}/*

%files         help
%defattr(-,root,root)
%doc README
%{_mandir}/*

%changelog
* Sun Jun 12 2022 YukariChiba <i@0x7f.cc> - 5.18.0-1
- Type:requirements
- ID:NA
- SUG:NA
- DESC: Upgrade version to 5.18.0

* Tue Mar 01 2022 jiangheng<jiangheng12@huawei.com> - 5.15.0-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: remove libcap-devel dependency

* Mon Feb 21 2022 jiangheng<jiangheng12@huawei.com> - 5.15.0-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: remove libdb-devel dependency

* Fri Nov 26 2021 jiangheng <jiangheng12@huawei.com> - 5.15.0-1
- DESC: update to 5.15.0

* Mon Aug 02 2021 chenyanpanHW <chenyanpan@huawei.com> - 5.10.0-2
- DESC: delete -S git from %autosetup, and delete BuildRequires git

* Tue Jan 26 2021 xihaochen<xihaochen@huawei.com> - 5.10.0-1
- Type:requirements
- ID:NA
- SUG:NA
- DESC: update iproute to 5.10.0

* Thu Dec 10 2020 zhouyihang <zhouyihang3@huawei.com> - 5.7.0-3
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:modify fix of get_tc_lib err

* Thu Sep 24 2020 zhouyihang <zhouyihang3@huawei.com> - 5.7.0-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:fix get_tc_lib err

* Wed Jul 22 2020 hanzhijun <hanzhijun1@huawei.com> - 5.7.0-1
- update to 5.7.0

* Mon Jan 20 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.4.0-2
- fix maddr show and change proc to ipnetnsproc

* Tue Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.4.0-1
- update to 5.4.0

* Fri Oct 18 2019 openEuler Buildteam <buildteam@openeuler.org> - 5.2.0-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add the bugfix about iproute

* Thu Sep 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 5.2.0-1
- Package init
